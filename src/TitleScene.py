import pygame
from GameObject import GameObject
import Input
import Settings
from Text import Text
from Button import Button
import Globals
from GameScene import GameScene
import FileManager

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
        
        self.resume_button = Button("images/startbutton_default.png", "images/startbutton_hover.png", 
                                "images/startbutton_click.png")
        self.resume_button.x = center[0] - self.resume_button.size[0]/2 + 120
        self.resume_button.y = center[1] - self.resume_button.size[1]/2 + 100
        self.resume_button.onclick = self.resume_clicked

        self.crown = GameObject("images/crown.png")
        self.crown.pos.x = center[0] - self.crown.size[0] / 2 - 50
        self.crown.pos.y = center[1] - self.crown.size[1] / 2 - 50

        self.text = Text(text = str(Globals.best_score), size = 40,
                         x = self.crown.pos.x + self.crown.size[0] + 20, y = self.crown.pos.y + 10)
    
    def button_clicked(self):
        Globals.change_scene(GameScene())

    def resume_clicked(self):
        Globals.change_scene(GameScene(FileManager.load_gamescene()))

    def update(self, delta_time):
        self.start_button.update()
        self.resume_button.update()

    def render(self, gameDisplay):
        self.bg.render(gameDisplay)
        self.text.render(gameDisplay)
        self.crown.render(gameDisplay)
        self.start_button.render(gameDisplay)
        self.resume_button.render(gameDisplay)