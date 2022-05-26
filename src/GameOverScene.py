from turtle import Turtle
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

class GameOverScene:
    def __init__(self, recent_score, isauto = False):
        self.recent_score = recent_score
        self.isauto = isauto
        pygame.mixer.music.stop()

        width = Settings.display_width
        height = Settings.display_height
        center = (width/2, height/2)

        self.bg = GameObject("images/gameoverscene/gameoverscene_bg.png",(int(width/4),int(height/4)))
        self.bg.set_size(int(width/2), int(height/2))
        
        self.recent_score = recent_score
        if DataManager.get_best_ranking() is None:
            self.best_score = 0
        else:
            self.best_score = DataManager.get_best_ranking()[1]


        self.win_sound = pygame.mixer.Sound("sounds/Tada.wav")
        self.lose_sound = pygame.mixer.Sound("sounds/lose.wav")
        self.win_sound.set_volume(0.5)
        self.lose_sound.set_volume(0.5)
       
        if recent_score > self.best_score:
            self.win_sound.play()
        else :
            self.lose_sound.play()

        self.gameover_text = Text("GameOver", 40, Vector2(center[0], 200), text_color, align= ALIGN_CENTER,)
        self.yourscore_text = Text("YOUR SCORE", 25, Vector2(300, 270), color = text_color, align=ALIGN_RIGHT)
        self.yourscore_score = Text(recent_score, 25, Vector2(400, 270), color = text_color, align=ALIGN_CENTER)
        self.bestscore_text = Text("BEST SCORE", 25, Vector2(300, 300), color = text_color, align=ALIGN_RIGHT)
        self.bestscore_score = Text(self.best_score, 25, Vector2(400, 300), color = text_color, align=ALIGN_CENTER)
     
        if not isauto and recent_score > 0:
            self.yourname_text = Text("Enter Your Name: ", fontsize = 25, pos = Vector2(center[0],340), color = text_color, align=ALIGN_RIGHT)
            self.username = EditText(x = center[0] + 20 , y = 340 - 5, width = 130, height = 30, text_size = 30, hint="Name", active = True)
        
            self.submit_button = BasicTextButton("Submit",flag = True)
            self.submit_button.pos = Vector2(center[0] - self.submit_button.size[0]/2, 400)
            self.submit_button.onclick = self.submit_clicked

            self.submit_text = Text("Submitted successfully!", fontsize = 25, pos = Vector2(center[0], 450), color = (30,30,30), align=ALIGN_CENTER)
            self.submitted = False

        #button
        #restart button
        self.restart_button = BasicTextButton("Restart",flag = True)
        self.restart_button.pos = Vector2(center[0] - 70 - self.restart_button.size[0]/2, center[1] + 140- self.restart_button.size[1]/2)
        self.restart_button.onclick = self.restartButton_clicked
        #exit button
        self.exit_button = BasicTextButton("Exit",flag = True)
        self.exit_button.pos = Vector2(center[0] + 70 - self.restart_button.size[0]/2, center[1] + 140 - self.restart_button.size[1]/2)
        self.exit_button.onclick = self.exitButton_clicked

    def submit_clicked(self):
        if self.submitted:
            return
        self.submitted = True
        name = self.username.text
        if self.username.text == "":
            name = "Player"
        DataManager.add_ranking(str(name), self.recent_score)

    def exitButton_clicked(self):
        from TitleScene import TitleScene
        Globals.change_scene(TitleScene())
    
    def restartButton_clicked(self):
        if self.isauto:
            from AutoGameScene import AutoGameScene
            Globals.change_scene(AutoGameScene())
        else:
            from GameScene import GameScene
            Globals.change_scene(GameScene())

    def update(self, delta_time):
        self.exit_button.update()
        self.restart_button.update()
        if self.recent_score > 0 and not self.isauto:
            self.username.update()
            self.submit_button.update()

    def render(self, gameDisplay):
        self.bg.render(gameDisplay)
        self.gameover_text.render(gameDisplay)
        self.yourscore_text.render(gameDisplay)
        self.yourscore_score.render(gameDisplay)
        self.bestscore_text.render(gameDisplay)
        self.bestscore_score.render(gameDisplay)
        if self.recent_score > 0 and not self.isauto:
            self.yourname_text.render(gameDisplay)
            self.username.render(gameDisplay)
            self.submit_button.render(gameDisplay)
            if self.submitted:
                self.submit_text.render(gameDisplay)
        #buttons
        self.exit_button.render(gameDisplay)
        self.restart_button.render(gameDisplay)

