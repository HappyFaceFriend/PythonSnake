import pygame
from pygame import Vector2

class GameObject:
    def __init__(self, image_path, x = 0, y = 0):
        self.image = pygame.image.load(image_path)
        self.pos = Vector2(x, y)
        self.size = self.image.get_rect().size
    def update(self, delta_time):
        pass
    def set_size(self, size):
        self.image = pygame.transform.scale(self.image, (int(size[0]), int(size[1])))
    def rotate(self, rot):
        self.image = pygame.transform.rotate(self.image, rot)
    def render(self, gameDisplay):
        gameDisplay.blit(self.image, self.pos)



        
