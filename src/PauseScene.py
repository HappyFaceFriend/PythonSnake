import pygame
from GameObject import GameObject
from TitleScene import TitleScene
from GameScene import GameScene
import Input
import Settings
from Text import Text, ALIGN_CENTER
from Button import Button
import Globals
import DataManager
from pygame import Vector2


class PauseScene:
    def __init__(self, gamescene):
        self.gamescene = gamescene

        self.bg = GameObject("images/pausescene_bg.png")
        self.bg.set_size(Settings.display_width, Settings.display_height)
        
        spacing = 50
        raw_texts = ["Restart", "Resume", "Save", "Exit"]
        onclicks = [self.restartButton_clicked, self.resumeButton_clicked, self.saveButton_clicked, self.exitButton_clicked]
        self.buttons = []
        self.texts = []
        for i in range(4):
            button = Button("images/buttonframe.png","images/buttonframe_hover.png","images/buttonframe_down.png")
            button.pos = Vector2(Settings.display_width / 2 - button.size[0]/2,
                                 140 + (spacing + button.size[1]) * i)
            button.onclick = onclicks[i]
            text = Text(raw_texts[i], 36, align = ALIGN_CENTER, bold=True, italic=True)
            text.pos = Vector2(Settings.display_width / 2, button.pos.y + button.size[1]/2 - text.size[1]/2)
            self.buttons.append(button)
            self.texts.append(text)

    def saveButton_clicked(self):
         DataManager.save_gamescene(self.gamescene)
         Globals.change_scene(TitleScene())

    def exitButton_clicked(self):
         Globals.change_scene(TitleScene())

    def restartButton_clicked(self):
         Globals.change_scene(GameScene())

    def resumeButton_clicked(self):
         self.gamescene.on_resume_game()
         Globals.change_scene(self.gamescene)


    def update(self, delta_time):
        for button in self.buttons:
            button.update()

    def render(self, gameDisplay):
        self.bg.render(gameDisplay)
        for button in self.buttons:
            button.render(gameDisplay)
        for text in self.texts:
            text.render(gameDisplay)

