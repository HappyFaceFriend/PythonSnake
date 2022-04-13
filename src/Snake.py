import pygame
import Settings
import Globals
from pygame import Vector2


class Snake:
    def __init__(self, initial_length):
        center = (Settings.board_size[0]/2,Settings.board_size[1]/2)
        self.body=[Vector2(center[0], center[1] + i) for i in range(initial_length)]
        self.dir=Vector2(0,-1)
        self.new_block = False
        self.last_dir = self.dir

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
        self.out_of_range()
        self.last_dir = self.dir

    def draw_snake(self):
        for block in self.body:
            x=int(20 + block.x * Settings.cell_size[0])
            y=int(100 + 20 + block.y * Settings.cell_size[1])
            block_rect=pygame.Rect(x, y, Settings.cell_size[0], Settings.cell_size[1])
            pygame.draw.rect(Globals.gameDisplay, 'yellow', block_rect)

    def add_snake(self):
        self.new_block=True
    
    def out_of_range(self):
        if not 0<=self.body[0].x<Settings.board_size[0] or not 0<=self.body[0].y<Settings.board_size[1]:
            pygame.quit()