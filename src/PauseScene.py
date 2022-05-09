import pygame
from GameObject import GameObject
from TitleScene import TitleScene
from GameScene import GameScene
from AutoGameScene import AutoGameScene
import Input
import Settings
from Text import Text, ALIGN_CENTER
from BasicTextButton import BasicTextButton
import Globals
import DataManager
from pygame import Vector2


class PauseScene:
     def __init__(self, gamescene, isauto = False):
          self.gamescene = gamescene
          self.isauto = isauto

          self.bg = GameObject("images/pausescene_bg.png")
          self.bg.set_size(Settings.display_width, Settings.display_height)
          
          spacing = 50
          raw_texts = ["Restart", "Resume", "Save", "Exit"]
          onclicks = [self.restartButton_clicked, self.resumeButton_clicked, self.saveButton_clicked, self.exitButton_clicked]
          self.buttons = []
          for i in range(len(raw_texts)):
               if isauto and raw_texts[i] == "Save":
                    continue
               button = BasicTextButton(raw_texts[i])
               button.pos = Vector2(Settings.display_width / 2 - button.size[0]/2,
                                   140 + (spacing + button.size[1]) * i)
               button.onclick = onclicks[i]
               self.buttons.append(button)

     def saveButton_clicked(self):
          DataManager.save_gamescene(self.gamescene)
          Globals.change_scene(TitleScene(saved = True))

     def exitButton_clicked(self):
          Globals.change_scene(TitleScene())

     def restartButton_clicked(self):
          if self.isauto:
               Globals.change_scene(AutoGameScene())
          else:
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

