import pygame
import Settings
import Globals
import time 
from pygame import Vector2


class Snake:
    def __init__(self, initial_length):
        center = (Settings.board_size[0]/2,Settings.board_size[1]/2)
        self.body=[Vector2(center[0], center[1] + i) for i in range(initial_length)]
        self.dir=Vector2(0,-1)
        self.new_block = False
        self.last_dir = self.dir
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
        self.check_gameover()
        self.last_dir = self.dir

    def draw_snake(self):
        index = 0
        for block in self.body:
            x=int(15 + block.x * Settings.cell_size[0])
            y=int(95 + 20 + block.y * Settings.cell_size[1])
           
            if index == 0 :
                snake_body = pygame.image.load("images/snake/head.png")
                if self.dir[0] == 1:
                    snake_body = pygame.transform.rotate(snake_body, 270)                 
                elif self.dir[0] == -1:
                    snake_body = pygame.transform.rotate(snake_body, 90)                 
                elif self.dir[1] == 1:
                    snake_body = pygame.transform.rotate(snake_body, 180)                 
                else:
                    pass

            elif index % 2 == 0:
                snake_body = pygame.image.load("images/snake/body2.png")
            elif index % 2 == 1:
                snake_body = pygame.image.load("images/snake/body1.png")
            Globals.gameDisplay.blit(snake_body, (x,y))
            index += 1

    def add_snake(self):
        self.new_block=True
    
    def check_gameover(self):
        if not 0<=self.body[0].x<Settings.board_size[0] or not 0<=self.body[0].y<Settings.board_size[1]:
            self.hit_sound.play()
            time.sleep(0.5)
            pygame.quit()

        for block in self.body[1:]:
            if block == self.body[0]:
                self.hit_sound.play()
                time.sleep(0.5)
                pygame.quit()

