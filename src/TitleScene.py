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
        self.start_button = Button("images/startbutton_default.png", "images/startbutton_hover.png", "images/startbutton_click.png", 50,50)
        self.start_button.onclick = self.button_clicked
        self.speed = 100
        self.text = Text(text = "0", size = 20)
        self.i = 0
    def button_clicked(self):
        self.i += 1
        self.text.text = str(self.i)
        if self.i == 5:
            Globals.change_scene(SampleScene())
    def update(self, delta_time):
        self.start_button.update()

    def render(self, gameDisplay):
        self.bg.render(gameDisplay)
        self.text.render(gameDisplay)
        self.start_button.render(gameDisplay)