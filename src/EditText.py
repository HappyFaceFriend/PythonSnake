import pygame
from pygame import Rect, Vector2
from Text import Text
import Input
import re

class EditText:
    def __init__(self, x, y, width, height, text_size, text='', hint = 'Input',
                inactive_border_color=(0,0,0), active_border_color=(0,0,255), 
                fill_color = (255,255,255), text_color = (0,0,0), hint_color=(120,120,120), max_len = 10, active= False):
        self.rect = Rect(x, y, width, height)
        self.text_size = text_size
        self.text = text
        self.hint = hint
        self.hint_color = hint_color
        self.inactive_border_color = inactive_border_color
        self.active_border_color = active_border_color
        self.fill_color = fill_color
        self.max_len = max_len
        self.text_object = Text(str(self.text), text_size, Vector2(x+5, y+5), color=text_color)
        self.hint_object = Text(str(self.hint), text_size, Vector2(x+5, y+5), color=hint_color)
        self.active = active

    def update(self, delta_time = 0):
        if Input.is_mouse_button_down():
            if self.rect.collidepoint(Input.get_mouse_pos()):
                self.active = True
            else:
                self.active = False
        elif self.active:
            for event in Input.events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.active = False
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    elif pygame.key.name(event.key).isalnum and len(pygame.key.name(event.key)) == 1 and len(self.text)<self.max_len:
                        self.text += pygame.key.name(event.key)
                        self.text = self.text.upper()
                        self.text = re.sub(r"[^A-Za-z0-9]", "", self.text)
                    #elif event.unicode.isalnum():
                    #    self.text += event.unicode
            
            self.text_object.text = self.text
            self.text_object.submit()
    
    def render(self, gameDisplay):
        pygame.draw.rect(gameDisplay, self.fill_color, self.rect)
        if self.active:
            pygame.draw.rect(gameDisplay, self.active_border_color, self.rect, 2)
        else:
            pygame.draw.rect(gameDisplay, self.inactive_border_color, self.rect, 2)
        if not self.active and len(self.text) == 0:
            self.hint_object.render(gameDisplay, False)
        else:
            self.text_object.render(gameDisplay, False)