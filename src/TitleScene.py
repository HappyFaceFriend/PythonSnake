import pygame
from GameObject import GameObject
import Input
import Settings
from Text import Text, ALIGN_CENTER
from Button import Button
import Globals
from GameScene import GameScene
from RankingScene import RankingScene
import DataManager
from pygame import Vector2

class TitleScene:
    def __init__(self):
        self.bg = GameObject("images/titlescene/bg.png")
        self.bg.set_size(Settings.display_width, Settings.display_height)
        
        spacing = 30
        raw_texts = ["Play", "Load", "Ranking", "Exit"]
        onclicks = [self.play_clicked, self.load_clicked, self.ranking_clicked, self.exit_clicked]
        self.buttons = []
        self.texts = []
        for i in range(4):
            button = Button("images/buttonframe.png","images/buttonframe_hover.png","images/buttonframe_down.png")
            button.pos = Vector2(Settings.display_width / 2 - button.size[0]/2,
                                 300 + (spacing + button.size[1]) * i)
            button.onclick = onclicks[i]
            text = Text(raw_texts[i], 36, align = ALIGN_CENTER, bold=True, italic=True)
            text.pos = Vector2(Settings.display_width / 2, button.pos.y + button.size[1]/2 - text.size[1]/2)
            self.buttons.append(button)
            self.texts.append(text)

    def update(self, delta_time):
        for button in self.buttons:
            button.update()

    def render(self, gameDisplay):
        self.bg.render(gameDisplay)
        for button in self.buttons:
            button.render(gameDisplay)
        for text in self.texts:
            text.render(gameDisplay)
        
    def play_clicked(self):
        Globals.change_scene(GameScene())

    def load_clicked(self):
        Globals.change_scene(GameScene(DataManager.load_gamescene()))

    def ranking_clicked(self):
        Globals.change_scene(RankingScene())

    def exit_clicked(self):
        Globals.quit_game()
