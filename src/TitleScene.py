import pygame
from GameObject import GameObject
import Input
import Settings
from Text import Text
from Button import Button
import Globals
from GameScene import GameScene
from RankingScene import RankingScene
import DataManager
from pygame import Vector2


class TitleScene:
    def __init__(self):
        self.bg = GameObject("images/titlescene/bg.png")
        self.bg.set_size((Settings.display_width, Settings.display_height))
        
        self.play_button = Button("images/titlescene/button_play.png")
        self.play_button.onclick = self.play_clicked
        self.load_button = Button("images/titlescene/button_load.png")
        self.load_button.onclick = self.load_clicked
        self.ranking_button = Button("images/titlescene/button_ranking.png")
        self.ranking_button.onclick = self.ranking_clicked
        self.exit_button = Button("images/titlescene/button_exit.png")
        self.exit_button.onclick = self.exit_clicked
        
        self.buttons = [self.play_button, self.load_button, self.ranking_button, self.exit_button]
        spacing = 30
        for i in range(len(self.buttons)):
            button = self.buttons[i]
            button.pos = Vector2(Settings.display_width / 2 - button.size[0]/2,
                                 300 + (spacing + button.size[1]) * i)

    def update(self, delta_time):
        for button in self.buttons:
            button.update()

    def render(self, gameDisplay):
        self.bg.render(gameDisplay)
        for button in self.buttons:
            button.render(gameDisplay)
        
    def play_clicked(self):
        Globals.change_scene(GameScene())

    def load_clicked(self):
        Globals.change_scene(GameScene(DataManager.load_gamescene()))

    def ranking_clicked(self):
        Globals.change_scene(RankingScene())

    def exit_clicked(self):
        Globals.quit_game()
