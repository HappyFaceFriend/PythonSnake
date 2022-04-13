import pygame
from GameObject import GameObject
import Input
import Settings
from Text import Text
from Button import Button
import Globals
from GameScene import GameScene

class TitleScene:
    def __init__(self):
        self.bg = GameObject("images/titlescene_bg.png")
        self.bg.set_size((Settings.display_width, Settings.display_height))
        center = (Settings.display_width / 2, Settings.display_height / 2)
        self.start_button = Button("images/startbutton_default.png", "images/startbutton_hover.png", 
                                "images/startbutton_click.png")
        self.start_button.x = center[0] - self.start_button.size[0]/2
        self.start_button.y = center[1] - self.start_button.size[1]/2 + 100
        self.start_button.onclick = self.button_clicked

        self.crown = GameObject("images/crown.png")
        self.crown.x = center[0] - self.crown.size[0] / 2 - 50
        self.crown.y = center[1] - self.crown.size[1] / 2 - 50

        self.speed = 100
        self.text = Text(text = str(Globals.best_score), size = 40,
                         x = self.crown.x + self.crown.size[0] + 20, y = self.crown.y + 10)
    
    def button_clicked(self):
        Globals.current_scene = GameScene()

    def update(self, delta_time):
        self.start_button.update()

    def render(self, gameDisplay):
        self.bg.render(gameDisplay)
        self.text.render(gameDisplay)
        self.crown.render(gameDisplay)
        self.start_button.render(gameDisplay)