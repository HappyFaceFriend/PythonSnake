from cgitb import text
from tkinter import CENTER
import pygame
from GameObject import GameObject
import Input
import Settings
import Globals
from Button import Button
from Text import ALIGN_CENTER
from Text import ALIGN_LEFT
from Text import ALIGN_RIGHT
from Text import Text 
from EditText import EditText
import DataManager 


text_color = (100,0,0)

class GameOverScene:
    def __init__(self, recent_score):
        self.recent_score = recent_score
        pygame.mixer.music.stop()

        width = Settings.display_width
        height = Settings.display_height
        center = (width/2, height/2)

        self.bg = GameObject("images/gameoverscene/gameoverscene_bg.png")
        self.bg.set_size((Settings.display_width, Settings.display_height))
        
        self.best_score = DataManager.get_best_ranking()

        self.win_sound = pygame.mixer.Sound("sounds/Tada.wav")
        self.lose_sound = pygame.mixer.Sound("sounds/lose.wav")
        self.win_sound.set_volume(0.5)
        self.lose_sound.set_volume(0.5)
       
        if recent_score > self.best_score[1] :
            self.win_sound.play()
        else :
            self.lose_sound.play()

        self.gameover_text = Text("GameOver", size = 50, x= center[0], y= center[1]/4, color = text_color, align= ALIGN_CENTER)
        self.yourscore_text = Text("YOUR SCORE", size = 30, x= center[0]/2, y= height/3, color = text_color, align=ALIGN_RIGHT)
        self.yourscore_score = Text(recent_score, size = 30, x= center[0]+center[0]/2, y= height/3, color = text_color, align=ALIGN_CENTER)
        self.bestscore_text = Text("BEST SCORE", size = 30, x= center[0]/2, y= height/3 + 50, color = text_color, align=ALIGN_RIGHT)
        self.bestscore_score = Text(self.best_score[1], size = 30, x= center[0]+center[0]/2, y= height/3 + 50, color = text_color, align=ALIGN_CENTER)
     

        self.yourname_text = Text("Your Name", size = 30, x = center[0]/2, y = center[1], color = text_color, align=ALIGN_RIGHT)
        self.username = EditText(x = center[0]+center[0]/2 + 30 , y = center[1], width = 30, height = 30, text_size = 30)
        
        print(Input.keyboard)

        #button
        #restart button
        self.restart_button = Button("images/button_restart.png", "images/button_restart.png", 
                                "images/button_restart.png")
        self.restart_button.pos.x = center[0] - self.restart_button.size[0]/2 -100
        self.restart_button.pos.y = center[1] - self.restart_button.size[1]/2 +150
        self.restart_button.onclick = self.restartButton_clicked
        #exit button
        self.exit_button = Button("images/button_exit.png", "images/button_exit.png", 
                                "images/button_exit.png")
        self.exit_button.pos.x = center[0] - self.exit_button.size[0]/2 +100
        self.exit_button.pos.y = center[1] - self.exit_button.size[1]/2 +150
        self.exit_button.onclick = self.exitButton_clicked
    
    def exitButton_clicked(self):
        from TitleScene import TitleScene
        DataManager.add_ranking(str(self.username.text), self.recent_score)
        Globals.change_scene(TitleScene())
    
    def restartButton_clicked(self):
        from GameScene import GameScene
        DataManager.add_ranking(str(self.username.text), self.recent_score)
        Globals.change_scene(GameScene())

    def update(self, delta_time):
        self.exit_button.update()
        self.restart_button.update()
        self.username.update(delta_time)

    def render(self, gameDisplay):
        self.bg.render(gameDisplay)
        self.gameover_text.render(gameDisplay)
        self.yourscore_text.render(gameDisplay)
        self.yourscore_score.render(gameDisplay)
        self.bestscore_text.render(gameDisplay)
        self.bestscore_score.render(gameDisplay)
        self.yourname_text.render(gameDisplay)
        self.username.render(gameDisplay)
        #buttons
        self.exit_button.render(gameDisplay)
        self.restart_button.render(gameDisplay)

