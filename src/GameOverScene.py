import pygame
from GameObject import GameObject
import Input
import Settings
from Text import Text
from Button import Button
import Globals


background_color = (150,150,255)
LIGHTBLUE = (0, 155, 155)
class GameOverScene:
    def __init__(self, recent_score):
        self.image_apple = pygame.image.load("images/snake/head.png")
        pygame.mixer.music.pause()
        pass
    
    def update(self, delta_time):
        pass

    def render(self, gameDisplay):
        gameDisplay.blit(self.image_apple, (50,50))
        pass