import pygame
from GameObject import GameObject
import Input
import Settings
from Text import Text
class SampleScene:
    def __init__(self):
        self.player = GameObject("images/icon.png")
        self.speed = 100
        self.text = Text(text = "0", size = 20)
        self.i = 0
    def update(self, delta_time):
        if Input.is_key_hold(pygame.K_UP):
            self.player.y -= self.speed * delta_time
        if Input.is_key_hold(pygame.K_DOWN):
            self.player.y += self.speed * delta_time
        if Input.is_key_hold(pygame.K_LEFT):
            self.player.x -= self.speed * delta_time
        if Input.is_key_hold(pygame.K_RIGHT):
            self.player.x += self.speed * delta_time
        if Input.is_key_down(pygame.K_UP):
            self.i += 1
            self.text.text = str(self.i)

    def render(self, gameDisplay):
        pygame.draw.rect(gameDisplay, (0,0,0), pygame.Rect(0, 0, Settings.display_width, Settings.display_height))
        self.player.render(gameDisplay) 
        self.text.render(gameDisplay)