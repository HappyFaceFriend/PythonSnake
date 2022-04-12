import pygame
import Settings

class Text:
    def __init__(self, text = "", size = 10, x = 0, y = 0, color = (255,255,255)):
        self.text = text
        self.size = size
        self.x = x
        self.y = y
        self.color = color
        

    def submit(self):   #조정 사항 반영
        self.fontInfo = pygame.font.Font(Settings.font_style, self.size)
        self.TextSurf = self.fontInfo.render(str(self.text), True, self.color)
        self.TextRect = self.TextSurf.get_rect()
        self.TextRect[0] += self.x
        self.TextRect[1] += self.y
        self.TextRect[2] += self.x
        self.TextRect[3] += self.y
        
    def render(self,gameDisplay):
        self.submit()
        gameDisplay.blit(self.TextSurf, self.TextRect)
    
        
