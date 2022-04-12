import pygame
from GameObject import GameObject
import Input
import Settings
from Text import Text
from Button import Button
import Globals
from SampleScene import SampleScene

class TitleScene:
    def __init__(self):
        self.bg = GameObject("images/titlescene_bg.png")
        center = (Settings.display_width/2 , Settings.display_height/2)
        self.start_button = Button("images/startbutton_default.png", "images/startbutton_hover.png", 
                                "images/startbutton_click.png", 200, 300)

        self.start_button.onclick = self.button_clicked

        self.crown = GameObject("images/crown.png", 160, 190)
        self.speed = 100
        self.text = Text(text = str(Globals.best_score), size = 40, x = 250, y = 200)
    def button_clicked(self):
        Globals.current_scene = SampleScene()
    def update(self, delta_time):
        self.start_button.update()

    def render(self, gameDisplay):
        self.bg.render(gameDisplay)
        self.text.render(gameDisplay)
        self.crown.render(gameDisplay)
        self.start_button.render(gameDisplay)