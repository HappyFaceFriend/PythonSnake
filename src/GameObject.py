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
        self.image = pygame.transform.scale(self.image, size)
    def rotate(self, rot):
        self.image = pygame.transform.rotate(self.image, rot)
    def render(self, gameDisplay):
        gameDisplay.blit(self.image, (self.x, self.y))

class Apple:
    def __init__(self):#implement image_path argument later
        self.x=random.randint(0,BOARD_SIZE -1)
        self.y=random.randint(0,BOARD_SIZE -1)
        self.pos=Vector2(self.x,self.y)
         
    def draw_apple(self):
        apple_rect=pygame.Rect(int(20+self.pos.x*CELL_SIZE),int(100+20+self.pos.y*CELL_SIZE),CELL_SIZE,CELL_SIZE)
        pygame.draw.rect(Globals.gameDisplay,'red',apple_rect)

