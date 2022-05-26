import pygame
from GameObject import GameObject
import Input
import Settings
import Globals
from BasicTextButton import BasicTextButton
from Text import ALIGN_CENTER
from Text import ALIGN_LEFT
from Text import ALIGN_RIGHT
from Text import Text 
from EditText import EditText
import DataManager 
from pygame import Vector2


text_color = (100,0,0)
text_color2 =(40,100,250)
#no score functionality on dual mode
class DGameOverScene:
    def __init__(self,snakeAdead,snakeBdead):
       
        self.snakeAdead=snakeAdead
        self.snakeBdead=snakeBdead

        pygame.mixer.music.stop()

        width = Settings.display_width
        height = Settings.display_height
        center = (width/2, height/2)

        self.bg = GameObject("images/gameoverscene/gameoverscene_bg.png")
        self.bg.set_size(Settings.display_width, Settings.display_height)

        self.win_sound = pygame.mixer.Sound("sounds/Tada.wav")
        self.win_sound.set_volume(0.5)
        self.win_sound.play()
      

        self.gameover_text = Text("GameOver", 60, Vector2(center[0], 130), text_color, align= ALIGN_CENTER)
        if snakeAdead and not snakeBdead:
            self.win_text=Text("Snake B win!",100,Vector2(center[0],center[1]-70),text_color2, align= ALIGN_CENTER,)
        if snakeBdead and not snakeAdead:
            self.win_text=Text("Snake A win!",100,Vector2(center[0],center[1]-70),text_color2, align= ALIGN_CENTER,)
        if snakeAdead and snakeBdead:
            self.win_text=Text("No Winners!",100,Vector2(center[0],center[1]-70),text_color2, align= ALIGN_CENTER,)
        
        #button
        #restart button
        self.restart_button = BasicTextButton("Restart")
        self.restart_button.pos = Vector2(center[0] - 100- self.restart_button.size[0]/2, center[1] + 180- self.restart_button.size[1]/2)
        self.restart_button.onclick = self.restartButton_clicked
        #exit button
        self.exit_button = BasicTextButton("Exit")
        self.exit_button.pos = Vector2(center[0] + 100 - self.restart_button.size[0]/2, center[1] + 180 - self.restart_button.size[1]/2)
        self.exit_button.onclick = self.exitButton_clicked
       
    def exitButton_clicked(self):
        from TitleScene import TitleScene
        Globals.change_scene(TitleScene())
    
    def restartButton_clicked(self):
        from DGameScene import DGameScene
        Globals.change_scene(DGameScene())

    def update(self, delta_time):
        self.exit_button.update()
        self.restart_button.update()

    def render(self, gameDisplay):
        self.bg.render(gameDisplay)
        self.gameover_text.render(gameDisplay)
        self.win_text.render(gameDisplay)

        #buttons
        self.exit_button.render(gameDisplay)
        self.restart_button.render(gameDisplay)


