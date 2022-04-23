import pygame
from GameObject import GameObject
from TitleScene import TitleScene
from GameScene import GameScene
import Input
import Settings
from Text import Text
from Button import Button
import Globals


class PauseScene:
    def __init__(self, gamescene):
        self.gamescene = gamescene

        self.bg = GameObject("images/pausescene_bg.png")
        self.bg.set_size((Settings.display_width, Settings.display_height))
        center = (Settings.display_width / 2, Settings.display_height / 2)
        
        #restart button
        self.restart_button = Button("images/button_restart.png", "images/button_restart.png", 
                                "images/button_restart.png")
        self.restart_button.x = center[0] - self.restart_button.size[0]/2
        self.restart_button.y = center[1] - self.restart_button.size[1]/2 -200
        self.restart_button.onclick = self.restartButton_clicked
        #resume button
        self.resume_button = Button("images/button_resume.png", "images/button_resume.png", 
                                "images/button_resume.png")
        self.resume_button.x = center[0] - self.resume_button.size[0]/2
        self.resume_button.y = center[1] - self.resume_button.size[1]/2 -70
        self.resume_button.onclick = self.resumeButton_clicked
        #save button
        self.save_button = Button("images/button_save.png", "images/button_save.png", 
                                "images/button_save.png")
        self.save_button.x = center[0] - self.save_button.size[0]/2
        self.save_button.y = center[1] - self.save_button.size[1]/2 +60
        self.save_button.onclick = self.saveButton_clicked
        #exit button
        self.exit_button = Button("images/button_exit.png", "images/button_exit.png", 
                                "images/button_exit.png")
        self.exit_button.x = center[0] - self.exit_button.size[0]/2
        self.exit_button.y = center[1] - self.exit_button.size[1]/2 +190
        self.exit_button.onclick = self.exitButton_clicked
   
    def saveButton_clicked(self):
         Globals.current_scene = self.gamescene
    def exitButton_clicked(self):
         Globals.current_scene = TitleScene()
    def restartButton_clicked(self):
         Globals.current_scene = GameScene()
    def resumeButton_clicked(self):
         self.gamescene.on_resume_game()
         Globals.current_scene = self.gamescene


    def update(self, delta_time):
        self.save_button.update()
        self.exit_button.update()
        self.restart_button.update()
        self.resume_button.update()

    def render(self, gameDisplay):
        self.bg.render(gameDisplay)
        self.save_button.render(gameDisplay)
        self.exit_button.render(gameDisplay)
        self.restart_button.render(gameDisplay)
        self.resume_button.render(gameDisplay)

