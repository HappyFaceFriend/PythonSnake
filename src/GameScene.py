import pygame
from GameObject import GameObject
from pygame import Vector2
import Input
import Settings
import Globals
from Text import Text
from Snake import Snake
from GameOverScene import GameOverScene
import DataManager
import random
import time


background_color = (150,150,255)
board_color = (50,255,50)
board_color2 = (150,255,150)

board_rect = pygame.Rect(20, 120, Settings.board_size[0] * Settings.cell_size[0], Settings.board_size[1] * Settings.cell_size[1])

move_interval = 0.1

initial_length = 4


def get_image_pos(board_pos):
    return Vector2(Settings.border_size + board_pos[0]*Settings.cell_size[0],
            Settings.topbar_height + Settings.border_size + board_pos[1]*Settings.cell_size[1])

class GameScene:
    def __init__(self, state_dict = None):
        self.crown = GameObject("images/crown.png", Settings.display_width / 2 + 170, 50)
        self.crown.set_size((self.crown.size[0] / 2, self.crown.size[1] / 2))
        best = DataManager.get_best_ranking()
        self.best_score_text = Text(str(0 if best is None else best[1]), 30, self.crown.pos.x + 35 , 50)
        
        self.apple=GameObject("images/apple.png")
        if state_dict is None:
            self.apple_boardpos = Vector2(0,0)
            self.spawn_apple()
            self.snake=Snake(initial_length)
            self.score = 0
        else:
            self.apple_boardpos = Vector2(state_dict['apple_boardpos'][0],state_dict['apple_boardpos'][1])
            self.apple.pos = Vector2(state_dict['apple_pos'][0], state_dict['apple_pos'][1])
            self.snake = Snake(initial_length, state_dict['snake'])
            self.score = state_dict['score']
        
        self.score_text = Text(str(self.score), 40, Settings.display_width / 2 , 40)
        self.tick = 0
        
        pygame.mixer.music.load("sounds/I Need a Stack.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        
        
        self.bite_sound = pygame.mixer.Sound("sounds/Bite.wav")
        self.bite_sound.set_volume(0.5)

    def update(self, delta_time):
        self.tick += delta_time
        if self.tick >= move_interval:
            self.snake.update()
            if self.snake.is_dead:
                self.on_gameover()
            self.check_apple_collision()
            self.tick -= move_interval

        if Input.is_key_down(pygame.K_UP):
            if self.snake.last_dir.y!=1:
                self.snake.dir=Vector2(0,-1)
        if Input.is_key_down(pygame.K_DOWN):
            if self.snake.last_dir.y!=-1:
                self.snake.dir=Vector2(0,1)
        if Input.is_key_down(pygame.K_LEFT):
            if self.snake.last_dir.x!=1:
                self.snake.dir=Vector2(-1,0)
        if Input.is_key_down(pygame.K_RIGHT):
            if self.snake.last_dir.x!=-1:
                self.snake.dir=Vector2(1,0)
        if Input.is_key_down(pygame.K_ESCAPE):
            self.pause_game()

    def spawn_apple(self):
        x = random.randint(0, Settings.board_size[0] -1)
        y = random.randint(0,Settings.board_size[1] -1)
        self.apple_boardpos = Vector2(x,y)
        self.apple.pos = get_image_pos((x,y))
        
      
    def check_apple_collision(self):
        if self.apple_boardpos == self.snake.body[0]:
            self.spawn_apple()
            self.snake.add_snake()
            self.bite_sound.play()
            self.add_score(1)
              
    def render(self, gameDisplay):
        self.render_backgrounds(gameDisplay)
        self.render_UIs(gameDisplay)
        self.apple.render(gameDisplay)
        if self.snake.is_dead==False:
            self.snake.render(gameDisplay)
        

    def add_score(self, score):
        self.score += score
        self.score_text.text = str(self.score)

    def render_backgrounds(self, gameDisplay):
        pygame.draw.rect(gameDisplay, background_color, pygame.Rect(0, 0, Settings.display_width, Settings.display_height))
        for i in range(Settings.board_size[1]):
            for j in range(Settings.board_size[0]):
                rect = pygame.Rect(board_rect.left + j * Settings.cell_size[0], board_rect.top + i * Settings.cell_size[1], Settings.cell_size[0], Settings.cell_size[1])
                if (i+j)%2 == 0:
                    pygame.draw.rect(gameDisplay, board_color, rect)
                else:
                    pygame.draw.rect(gameDisplay, board_color2, rect)
                    
    def render_UIs(self, gameDisplay):
        self.crown.render(gameDisplay)
        self.best_score_text.render(gameDisplay)
        self.score_text.render(gameDisplay)

    def pause_game(self):
        pygame.mixer.music.pause()
        
        from PauseScene import PauseScene
        Globals.change_scene(PauseScene(self))

    def on_resume_game(self):
        pygame.mixer.music.play(-1)

    def on_gameover(self):
        Globals.change_scene(GameOverScene(self.score))
        
    def get_state_dict(self):
        state = {}
        state['score'] = self.score
        state['apple_pos'] = (self.apple.pos.x, self.apple.pos.y)
        state['apple_boardpos'] = (self.apple_boardpos.x, self.apple_boardpos.y)
        state['snake'] = self.snake.get_state_dict()
        return state
