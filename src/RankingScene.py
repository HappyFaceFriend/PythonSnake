import pygame
from GameObject import GameObject
import Input
import Settings
from Text import ALIGN_CENTER, Text
from Button import Button
import Globals
import DataManager
from pygame import Vector2

bg_color = (153,217,234)
header_color = (185,122,87)
text_color = (40,40,40)
line_color = (255,255,255)

start_y = 150
spacing = 20
header_size = 30
text_x = (180, 290, 430)
text_size = 25
line_x = (150, 480)

class RankingScene:
    def __init__(self):
        self.panel = GameObject("images/rankingscene/panel.png")
        self.panel.pos = Vector2(Settings.display_width / 2 - self.panel.size[0]/2, Settings.display_height / 2 - self.panel.size[1]/2 - 30)
        
        self.back_button = Button("images/rankingscene/button_back.png")
        self.back_button.onclick = self.back_clicked
        self.back_button.pos = Vector2(Settings.display_width / 2 - self.back_button.size[0]/2, Settings.display_height - 80)

        show_count = 5
        ranking = DataManager.ranking
        self.texts = []
        self.lines = []
        self.texts.append(Text("#", header_size, text_x[0] , start_y, color = header_color, align = ALIGN_CENTER))
        self.texts.append(Text("Name", header_size, text_x[1] , start_y, color = header_color, align = ALIGN_CENTER))
        self.texts.append(Text("Score", header_size, text_x[2] , start_y, color = header_color, align = ALIGN_CENTER))
        self.lines.append(150 + text_size + spacing/2)
        for i in range(len(ranking)):
            y = start_y + (text_size+spacing)*(i+1)
            self.texts.append(Text(str(i+1), text_size, text_x[0] , y, color=text_color, align = ALIGN_CENTER))
            self.texts.append(Text(ranking[i][0], text_size, text_x[1] , y, color=text_color,align = ALIGN_CENTER))
            self.texts.append(Text(str(ranking[i][1]), text_size, text_x[2] , y, color=text_color,align = ALIGN_CENTER))
            if i >= show_count-1:
                break
            self.lines.append(y + text_size + spacing/2)


    def update(self, delta_time):
        self.back_button.update()

    def render(self, gameDisplay):
        pygame.draw.rect(gameDisplay, bg_color, [0, 0, Settings.display_width, Settings.display_height])
        self.panel.render(gameDisplay)
        self.back_button.render(gameDisplay)
        for text in self.texts:
            text.render(gameDisplay, False)
        for y in self.lines:
            pygame.draw.line(gameDisplay, line_color, [line_x[0],y], [line_x[1],y])

    def back_clicked(self):
        from TitleScene import TitleScene
        Globals.change_scene(TitleScene())
