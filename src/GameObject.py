import pygame
from pygame import Vector2

class GameObject:
    def __init__(self, image_path, pos = Vector2(0,0)):
        self.image = pygame.image.load(image_path)
        self.pos = pos
        self.size = self.image.get_rect().size

    def update(self, delta_time):
        pass
    def set_size(self, width, height):
        self.image = pygame.transform.scale(self.image, (int(width), int(height)))
        self.size = self.image.get_rect().size

    def rotate(self, rot):
        self.image = pygame.transform.rotate(self.image, rot)

    def render(self, gameDisplay):
        gameDisplay.blit(self.image, self.pos)



        
