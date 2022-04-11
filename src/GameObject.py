import pygame

class GameObject:
    def __init__(self, image_path, x = 0, y = 0):
        self.image = pygame.image.load(image_path)
        self.x = x
        self.y = y
        self.size = self.image.get_rect().size
    def update(self, delta_time):
        pass
    def render(self, gameDisplay):
        gameDisplay.blit(self.image, (self.x, self.y))