import pygame
import Settings
from pygame import Vector2

ALIGN_LEFT = 0
ALIGN_RIGHT = 2
ALIGN_CENTER = 1
class Text:
    def __init__(self, text = "", fontsize = 10, pos=Vector2(0,0), color = (255,255,255),
                     align=ALIGN_LEFT, bold = False, italic = False):
        self.text = text
        self.fontsize = fontsize
        self.pos = pos
        self.color = color
        self.bold = bold
        self.italic = italic
        if align == ALIGN_LEFT:
            self.align_alpha = 0
        elif align == ALIGN_RIGHT:
            self.align_alpha = -1
        elif align == ALIGN_CENTER:
            self.align_alpha = -0.5
        self.submit()
        self.size = (self.TextRect.width, self.TextRect.height)

    def align_right(self):
        self.align_alpha = -1
    def align_left(self):
        self.align_alpha = 0
    def align_center(self):
        self.align_alpha = -0.5

    def submit(self):   #조정 사항 반영
        self.fontInfo = pygame.font.SysFont(Settings.font_style, self.fontsize, bold = self.bold, italic = self.italic)
        self.TextSurf = self.fontInfo.render(str(self.text), True, self.color)
        self.TextRect = self.TextSurf.get_rect()
        self.TextRect[0] += self.pos.x + self.align_alpha * width 
        self.TextRect[1] += self.pos.y
        self.TextRect[2] += self.pos.x + self.align_alpha * width 
        self.TextRect[3] += self.pos.y
        
    def render(self, gameDisplay, do_submit = True):
        if do_submit:
            self.submit()
        gameDisplay.blit(self.TextSurf, self.TextRect)
    
        
