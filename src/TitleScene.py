import pygame
from AutoGameScene import AutoGameScene
from DGameScene import DGameScene
from GameObject import GameObject
import Input
import Settings
from Text import Text, ALIGN_CENTER
from Button import Button
import Globals
from GameScene import GameScene
from AutoGameScene import AutoGameScene
from RankingScene import RankingScene
import DataManager
from pygame import Vector2
from BasicTextButton import BasicTextButton

class TitleScene:
    def __init__(self, saved = False):
        self.bg = GameObject("images/titlescene/bg.png")
        self.bg.set_size(Settings.display_width, Settings.display_height)
        self.saved = saved
        spacing = 30
        raw_texts = ["Single Play", "Dual Play", "Auto Play", "Load", "Ranking", "Exit"]
        onclicks = [self.play_clicked, self.Dplay_clicked ,self.auto_clicked, self.load_clicked, self.ranking_clicked, self.exit_clicked]
        self.buttons = []
        for i in range(len(raw_texts)):
            button = BasicTextButton(raw_texts[i])
            button.pos = Vector2(Settings.display_width / 2 - button.size[0]/2, 300 + (spacing + button.size[1]) * i)
            button.onclick = onclicks[i]
            self.buttons.append(button)
        self.savetext = Text("Game is saved.", 30, Vector2(Settings.display_width/2, 260), color = (50,50,50), align = ALIGN_CENTER)

    def update(self, delta_time):
        for button in self.buttons:
            button.update()

    def render(self, gameDisplay):
        self.bg.render(gameDisplay)
        for button in self.buttons:
            button.render(gameDisplay)
        if self.saved:
            self.savetext.render(gameDisplay)
        
    def play_clicked(self):
        Globals.change_scene(GameScene())

    def Dplay_clicked(self):
        Globals.change_scene(DGameScene())

    def auto_clicked(self):
        Globals.change_scene(AutoGameScene())

    def load_clicked(self):
        Globals.change_scene(GameScene(DataManager.load_gamescene()))

    def ranking_clicked(self):
        Globals.change_scene(RankingScene())

    def exit_clicked(self):
        Globals.quit_game()
