from typing import Set
from Button import Button
from pygame import Vector2
from Text import Text, ALIGN_CENTER
import Settings

class BasicTextButton(Button):
    def __init__(self, text = "", pos = Vector2(0,0), flag = None):
        self.text = text
        if flag:
            super().__init__(Settings.f2_path,Settings.f2_hover_path,Settings.f2_down_path)
            self.text_object = Text(text, 25, align = ALIGN_CENTER, bold = True, italic=True)
        else:
            super().__init__(Settings.f_path, Settings.f_hover_path, Settings.f_down_path)
            self.text_object = Text(text, 36, align = ALIGN_CENTER, bold = True, italic=True)

    def update(self, delta_time = 0):
        super().update()
        self.text_object.pos = self.pos + Vector2(self.size[0]/2, self.size[1]/2 - self.text_object.size[1]/2)
    
    def render(self, gameDisplay):
        super().render(gameDisplay)
        self.text_object.render(gameDisplay)

