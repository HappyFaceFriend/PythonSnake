import pygame
import Settings

ALIGN_LEFT = 0
ALIGN_RIGHT = 2
ALIGN_CENTER = 1
class Text:
    def __init__(self, text = "", size = 10, x = 0, y = 0, color = (255,255,255), align=ALIGN_LEFT):
        self.text = text
        self.size = size
        self.x = x
        self.y = y
        self.color = color
        if align == ALIGN_LEFT:
            self.align_alpha = -1
        elif align == ALIGN_RIGHT:
            self.align_alpha = 0
        elif align == ALIGN_CENTER:
            self.align_alpha = -0.5
        self.submit()
    def align_right(self):
        self.align_alpha = -1
    def align_left(self):
        self.align_alpha = 0
    def align_center(self):
        self.align_alpha = -0.5

    def submit(self):   #조정 사항 반영
        self.fontInfo = pygame.font.Font(Settings.font_style, self.size)
        self.TextSurf = self.fontInfo.render(str(self.text), True, self.color)
        self.TextRect = self.TextSurf.get_rect()
        width = self.TextRect.width
    
        self.TextRect[0] += self.x + self.align_alpha * width 
        self.TextRect[1] += self.y 
        self.TextRect[2] += self.x + self.align_alpha * width 
        self.TextRect[3] += self.y 
        
    def render(self, gameDisplay, do_submit = True):
        if do_submit:
            self.submit()
        gameDisplay.blit(self.TextSurf, self.TextRect)
    
        
