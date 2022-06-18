import pygame
from DGameOverScene import DGameOverScene
import Settings
import Globals
import time 
from pygame import Vector2


class DSnake:
    def __init__(self, initial_length, snake_number, state_dict = None):
        center = (Settings.Dboard_size[0]/2, Settings.Dboard_size[1]/2)
        print(state_dict)
        if state_dict is None:
            self.body=[Vector2(center[0] , center[1] + i) for i in range(initial_length)]
            self.dir=Vector2(0,-1)
            self.last_dir = self.dir
            self.is_dead = False
        else:
            self.body = [Vector2(x[0],x[1]) for x in state_dict['body']]
            self.dir = Vector2(state_dict['dir'][0], state_dict['dir'][1])
            self.last_dir = Vector2(state_dict['last_dir'][0], state_dict['last_dir'][1])
            self.is_dead = state_dict['is_dead']

        self.image_head = pygame.image.load("images/dualmode/dual_head.png")
        if (snake_number == 2):
            self.image_body = [pygame.image.load("images/dualmode/dual_body2.png"), pygame.image.load("images/dualmode/dual_body1B.png")]
        else:
            self.image_body = [pygame.image.load("images/dualmode/dual_body2.png"), pygame.image.load("images/dualmode/dual_body1A.png")]
        self.new_block = False
        self.hit_sound = pygame.mixer.Sound("sounds/Big Boing.wav")

    def update(self):
        if self.new_block ==True:
            copy=self.body[:]
            copy.insert(0, copy[0] + self.dir)
            self.body=copy[:]
            self.new_block =False
        else: 
            copy=self.body[:-1]
            copy.insert(0, copy[0] + self.dir)
            self.body=copy[:]
        self.last_dir = self.dir
        
        if self.check_death():
            self.hit_sound.play()
            self.is_dead = True
            time.sleep(0.3)
            Globals.change_scene(DGameOverScene)

    def check_death(self):
        if not 0<=self.body[0].x<Settings.Dboard_size[0] or not 0<=self.body[0].y<Settings.Dboard_size[1]:
            return True
        for block in self.body[1:]:
            if block == self.body[0]:
                return True
        return False
        
    def set_dir(self, dir):
        if dir == Vector2(0,-1) and self.last_dir.y == 1:
            return
        if dir == Vector2(0,1) and self.last_dir.y == -1:
            return
        if dir == Vector2(-1, 0) and self.last_dir.x == 1:
            return
        if dir == Vector2(1, 0) and self.last_dir.x == -1:
            return
        self.dir = dir
        
    def render(self, gameDisplay):
        index = 0
        for block in self.body:
            x=int(160 + block.x * Settings.Dcell_size[0])
            y=int(50 + block.y * Settings.Dcell_size[1])
           
            if index == 0 :
                snake_body = self.image_head
                if self.dir[0] == 1:
                    snake_body = pygame.transform.rotate(snake_body, 270)                 
                elif self.dir[0] == -1:
                    snake_body = pygame.transform.rotate(snake_body, 90)                 
                elif self.dir[1] == 1:
                    snake_body = pygame.transform.rotate(snake_body, 180)                 
                else:
                    pass

            else:
                snake_body = self.image_body[index % 2]
            gameDisplay.blit(snake_body, (x,y))
            index += 1

    def add_snake(self):
        self.new_block=True
    
    def get_state_dict(self):
        state = {}
        state['body'] = [ (cell.x, cell.y) for cell in self.body]
        state['dir'] = (self.dir.x, self.dir.y)
        state['last_dir'] = (self.last_dir.x, self.last_dir.y)
        state['is_dead'] = self.is_dead
        return state
