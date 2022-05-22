import pygame
from GameObject import GameObject
from pygame import Vector2
import Input
import Settings
import Globals
from Text import Text
from DSnake import DSnake
from GameOverScene import GameOverScene
import DataManager
import random

background_color = (150,150,255)
board_color = (50,255,50)
board_color2 = (150,255,150)

Dboard_rect = pygame.Rect(160, 50, Settings.Dboard_size[0] * Settings.Dcell_size[0], Settings.Dboard_size[1] * Settings.Dcell_size[1])

move_interval = 0.1

initial_length = 4


def get_image_pos(board_pos):
    return Vector2(160 + board_pos[0]*Settings.Dcell_size[0],
                   50 + board_pos[1]*Settings.Dcell_size[1])

class DGameScene:
    def __init__(self,state_dict=None):  
        
        self.appleA=GameObject("images/dualmode/dual_apple.png")
        self.appleB=GameObject("images/dualmode/dual_apple.png")

        if state_dict is None:
            self.appleA_boardpos = Vector2(0,0)
            self.appleB_boardpos = Vector2(0,0)
            self.snakeA=DSnake(initial_length)
            self.snakeA.body=[Vector2(5 , 5 - i) for i in range(initial_length)]
            self.snakeA.dir=Vector2(0,1)
            self.snakeA.last_dir = self.snakeA.dir
            self.snakeB=DSnake(initial_length)
            self.snakeB.body=[Vector2(Settings.Dboard_size[0] -5 , Settings.Dboard_size[1] -6  + i) for i in range(initial_length)]
            self.snakeB.dir=Vector2(0,-1)
            self.snakeB.last_dir = self.snakeB.dir
            
            self.spawn_appleA()
            self.spawn_appleB()
        else:
            self.appleA_boardpos = Vector2(state_dict['appleA_boardpos'][0],state_dict['appleA_boardpos'][1])
            self.appleA.pos = Vector2(state_dict['appleA_pos'][0], state_dict['appleA_pos'][1])
            self.appleB_boardpos = Vector2(state_dict['appleB_boardpos'][0],state_dict['appleB_boardpos'][1])
            self.appleB.pos = Vector2(state_dict['appleB_pos'][0], state_dict['appleB_pos'][1])
            self.snakeA = DSnake(initial_length, state_dict['snakeA'])
            self.snakeB = DSnake(initial_length, state_dict['snakeB'])
        
        self.tick = 0
        
        pygame.mixer.music.load("sounds/Banjo-Menu-Loop.wav")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        
        
        self.bite_sound = pygame.mixer.Sound("sounds/Bite.wav")
        self.bite_sound.set_volume(0.5)
        self.hit_sound = pygame.mixer.Sound("sounds/Big Boing.wav")

    def update(self, delta_time):
        self.tick += delta_time
        if self.tick >= move_interval:
            self.snakeA.update()
            self.snakeB.update()
            self.check_snake_collision()
            if self.snakeA.is_dead or self.snakeB.is_dead:
                self.on_gameover()
            self.check_apple_collision()
            self.tick -= move_interval
        
        #Snake A 
        if Input.is_key_down(pygame.K_UP):
            self.snakeB.set_dir(Vector2(0,-1))
        if Input.is_key_down(pygame.K_DOWN):
            self.snakeB.set_dir(Vector2(0,1))
        if Input.is_key_down(pygame.K_LEFT):
            self.snakeB.set_dir(Vector2(-1,0))
        if Input.is_key_down(pygame.K_RIGHT):
            self.snakeB.set_dir(Vector2(1,0))
        #Snake B
        if Input.is_key_down(pygame.K_w):
            self.snakeA.set_dir(Vector2(0,-1))
        if Input.is_key_down(pygame.K_s):
            self.snakeA.set_dir(Vector2(0,1))
        if Input.is_key_down(pygame.K_a):
            self.snakeA.set_dir(Vector2(-1,0))
        if Input.is_key_down(pygame.K_d):
            self.snakeA.set_dir(Vector2(1,0))
            
        if Input.is_key_down(pygame.K_ESCAPE):
            self.pause_game() 

    def spawn_appleA(self):
        retry = True
        while retry:
            x = random.randint(0, Settings.Dboard_size[0] -1)
            y = random.randint(0, Settings.Dboard_size[1] -1)
            retry = False
            for cell in self.snakeA.body:
                if cell == Vector2(x,y):
                    retry = True
                    break
            for cell in self.snakeB.body:
                if cell == Vector2(x,y):
                    retry = True
                    break
            if self.appleB_boardpos==Vector2(x,y):
                retry = True   

        self.appleA_boardpos = Vector2(x,y)
        self.appleA.pos = get_image_pos((x,y))
  

    def spawn_appleB(self):
        retry = True
        while retry:
            X = random.randint(0, Settings.Dboard_size[0] -1)
            Y = random.randint(0, Settings.Dboard_size[0] -1)
            retry = False
            for cell in self.snakeA.body:
                if cell == Vector2(X,Y):
                    retry = True
                    break
            for cell in self.snakeB.body:
                if cell == Vector2(X,Y):
                    retry = True
                    break
            if self.appleA_boardpos==Vector2(X,Y):
                retry = True

        self.appleB_boardpos = Vector2(X,Y)
        self.appleB.pos = get_image_pos((X,Y))
        

    def check_apple_collision(self):
        
        if self.appleA_boardpos == self.snakeA.body[0]:
            self.spawn_appleA()
            self.snakeA.add_snake()
            self.bite_sound.play()
        
        if self.appleA_boardpos == self.snakeB.body[0]: 
            self.spawn_appleA()
            self.snakeB.add_snake()
            self.bite_sound.play()

        if self.appleB_boardpos == self.snakeA.body[0]:
            self.spawn_appleB()
            self.snakeA.add_snake()
            self.bite_sound.play()
        
        if self.appleB_boardpos == self.snakeB.body[0]:
            self.spawn_appleB()
            self.snakeB.add_snake()
            self.bite_sound.play()
           
    def check_snake_collision(self):
         for cell in self.snakeA.body:
             if cell == self.snakeB.body[0]:
                 self.snakeB.is_dead=True
                 self.hit_sound.play()
                
         for cell in self.snakeB.body:
             if cell == self.snakeA.body[0]:
                 self.snakeA.is_dead=True
                 self.hit_sound.play()

         if self.snakeA.body[0]==self.snakeB.body[0]:
              self.snakeA.is_dead=True
              self.snakeB.is_dead=True
         
 
                
    def render(self, gameDisplay):
        self.render_backgrounds(gameDisplay)
        self.appleA.render(gameDisplay)
        self.appleB.render(gameDisplay)
        if self.snakeA.is_dead==False:
            self.snakeA.render(gameDisplay)
        if self.snakeB.is_dead==False:
            self.snakeB.render(gameDisplay)
        

    def render_backgrounds(self, gameDisplay):
        pygame.draw.rect(gameDisplay, background_color, pygame.Rect(0, 0, Settings.display_width, Settings.display_height))
        for i in range(Settings.Dboard_size[1]):
            for j in range(Settings.Dboard_size[0]):
                rect = pygame.Rect(Dboard_rect.left + j * Settings.Dcell_size[0], Dboard_rect.top + i * Settings.Dcell_size[1], Settings.Dcell_size[0], Settings.Dcell_size[1])
                if (i+j)%2 == 0:
                    pygame.draw.rect(gameDisplay, board_color, rect)
                else:
                    pygame.draw.rect(gameDisplay, board_color2, rect)
                    
    def pause_game(self):
        pygame.mixer.music.pause()
        
        from DPauseScene import DPauseScene
        Globals.change_scene(DPauseScene(self))

    def on_resume_game(self):
        pygame.mixer.music.play(-1)
    
    def on_gameover(self):
        from DGameOverScene import DGameOverScene
        if self.snakeA.is_dead and not self.snakeB.is_dead:
            Globals.change_scene(DGameOverScene(True, False))
        elif self.snakeB.is_dead and not self.snakeA.is_dead:
            Globals.change_scene(DGameOverScene(False, True))
        elif self.snakeB.is_dead and self.snakeA.is_dead:
            Globals.change_scene(DGameOverScene(True, True))
        
        
    def get_state_dict(self):
        state = {}
        state['appleA_pos'] = (self.appleA.pos.x, self.appleA.pos.y)
        state['appleA_boardpos'] = (self.appleA_boardpos.x, self.appleA_boardpos.y)
        state['appleB_pos'] = (self.appleB.pos.x, self.appleB.pos.y)
        state['appleB_boardpos'] = (self.appleB_boardpos.x, self.appleB_boardpos.y)
        state['snakeA'] = self.snakeA.get_state_dict()
        state['snakeB'] = self.snakeB.get_state_dict()
        return state

