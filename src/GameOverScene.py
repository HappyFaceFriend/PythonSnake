from cgitb import text
from tkinter import CENTER
import pygame
from GameObject import GameObject
import Input
import Settings
from Text import Text
from Button import Button
import Globals

class GameOverScene:
    def __init__(self, recent_score):
        pygame.mixer.music.stop()

        self.bg = GameObject("images/gameoverscene/gameoverscene_bg.png")
        self.bg.set_size((Settings.display_width, Settings.display_height))
        
        font = pygame.font.Font("fonts/arial.ttf", 60)
        self.text = font.render("game over", True, (100,0,0))
        text_size = self.text.get_rect().size
        text_width = text_size[0]
        text_height = text_size[1]
        self.text_pos = (Settings.display_width/2 - text_width/2, Settings.display_height/4 - text_height/2)

        self.text2 = font.render(str(recent_score), True, (100,0,0))

    def update(self, delta_time):
        pass

    def render(self, gameDisplay):
        self.bg.render(gameDisplay)
        gameDisplay.blit(self.text, self.text_pos)
        gameDisplay.blit(self.text2, self.text_pos)
    
  