from typing import Sequence
import pygame

def get_mouse_pos():
    return mouse.pos
def is_mouse_button_down():
    return mouse.event == MOUSE_DOWN
def is_mouse_button_hold():
    return mouse.event == MOUSE_DOWN or mouse.event == MOUSE_HOLD
def is_mouse_button_up():
    return mouse.event == MOUSE_UP
    
def is_key_down(keycode):
    return keyboard.current[keycode]==1 and keyboard.last[keycode]==0
def is_key_hold(keycode):
    return keyboard.current[keycode]==1
def is_key_up(keycode):
    return keyboard.current[keycode]==0 and keyboard.last[keycode]==1

#Constants
MOUSE_DOWN = 2
MOUSE_HOLD = 1
MOUSE_NONE = 0
MOUSE_UP = -1

KEY_DOWN = 2
KEY_HOLD = 1
KEY_NONE = 0
KEY_UP = -1

KEY_COUNT = 323


class MouseInput:
    def __init__(self):
        self.pos = (0,0)
        self.event = MOUSE_NONE
        self.last = 0
    def update(self):
        self.pos = pygame.mouse.get_pos()
        current = pygame.mouse.get_pressed()[0]
        if current == 1 and self.last == 0:
            self.event = MOUSE_DOWN
        elif current == 1 and self.last == 1:
            self.event = MOUSE_HOLD
        elif current == 0 and self.last == 1:
            self.event = MOUSE_UP
        elif current == 0 and self.last == 0:
            self.event = MOUSE_NONE
        self.last = current

class KeyboardInput:
    def __init__(self):
        self.last = []
        self.current = []
    def update(self):
        self.current = pygame.key.get_pressed()
    def late_update(self):
        self.last = self.current


mouse = MouseInput()
keyboard = KeyboardInput()
events = []