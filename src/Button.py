import pygame
import Input

BUTTON_DEFAULT = 0
BUTTON_HOVER = 1
BUTTON_CLICK = 2

class Button:
    def __init__(self, default_image_path, hover_image_path = "", click_image_path = "", x = 0, y = 0):
        self.images = {"default": pygame.image.load(default_image_path)}
        if hover_image_path != "":
            self.images["hover"] = pygame.image.load(hover_image_path)
        if click_image_path != "":
            self.images["click"] = pygame.image.load(click_image_path)
        self.current_image = self.images["default"]
        self.x = x
        self.y = y
        self.size = self.current_image.get_rect().size
        self.state = BUTTON_DEFAULT
        self.is_clicking = False
    def update(self):
        if self.is_mouse_bound():
            if self.state == BUTTON_DEFAULT:
                self.set_state(BUTTON_HOVER)
            if Input.is_mouse_button_down():
                self.is_clicking = True
                self.set_state(BUTTON_CLICK)
            elif Input.is_mouse_button_up() and self.is_clicking:
                self.onclick()
                self.set_state(BUTTON_HOVER)
        else:
            self.set_state(BUTTON_DEFAULT)

    def onclick(self):
        pass

    def set_state(self, state):
        if self.state == state:
            return
        self.state = state
        if state == BUTTON_DEFAULT:
            self.current_image = self.images["default"]
        elif state == BUTTON_HOVER:
            if "hover" in self.images.keys():
                self.current_image = self.images["hover"]
        elif state == BUTTON_CLICK:
            if "click" in self.images.keys():
                self.current_image = self.images["click"]

    def is_mouse_bound(self):
        mouse_pos = Input.get_mouse_pos()
        if (mouse_pos[0] >= self.x and mouse_pos[0] <= self.x+self.size[0] and
             self.y <= mouse_pos[1] and self.y+self.size[1] >= mouse_pos[1]):
            return True
        else:
            return False

    def render(self, gameDisplay):
        gameDisplay.blit(self.current_image, (self.x, self.y))