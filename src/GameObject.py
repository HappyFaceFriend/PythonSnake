import pygame
import random
import Settings
import Globals
from pygame import Vector2
#board constants
BOARD_SIZE=40
CELL_SIZE=15

class GameObject:
    def __init__(self, image_path, x = 0, y = 0):
        self.image = pygame.image.load(image_path)
        self.x = x
        self.y = y
        self.size = self.image.get_rect().size
    def update(self, delta_time):
        pass
    def set_size(self, size):
        self.image = pygame.transform.scale(self.image, (int(size[0]), int(size[1])))
    def rotate(self, rot):
        self.image = pygame.transform.rotate(self.image, rot)
    def render(self, gameDisplay):
        gameDisplay.blit(self.image, (self.x, self.y))

class Apple:
    def __init__(self):#implement image_path argument later
       self.random_spawn()
         
    def draw_apple(self):
        apple_rect=pygame.Rect(int(20+self.pos.x*CELL_SIZE),int(100+20+self.pos.y*CELL_SIZE),CELL_SIZE,CELL_SIZE)
        pygame.draw.rect(Globals.gameDisplay,'red',apple_rect)

    def random_spawn(self):
        self.x=random.randint(0,BOARD_SIZE -1)
        self.y=random.randint(0,BOARD_SIZE -1)
        self.pos=Vector2(self.x,self.y)

class Snake:
    def __init__(self):
        self.body=[Vector2(BOARD_SIZE/2,BOARD_SIZE/2),Vector2(BOARD_SIZE/2,BOARD_SIZE/2 -1),
                   Vector2(BOARD_SIZE/2,BOARD_SIZE/2 -2),Vector2(BOARD_SIZE/2,BOARD_SIZE/2 -3)]
        self.dir=Vector2(0,-1)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x=int(20+block.x*CELL_SIZE)
            y=int(100+20+block.y*CELL_SIZE)
            block_rect=pygame.Rect(x,y,CELL_SIZE,CELL_SIZE)
            pygame.draw.rect(Globals.gameDisplay,'yellow',block_rect)

    def move_snake(self):
        if self.new_block ==True:
            copy=self.body[:]
            copy.insert(0,copy[0]+self.dir)
            self.body=copy[:]
            self.new_block =False
        else: 
            copy=self.body[:-1]
            copy.insert(0,copy[0]+self.dir)
            self.body=copy[:]
         
    def add_snake(self):
        self.new_block=True

        
