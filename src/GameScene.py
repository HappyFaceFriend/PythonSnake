import pygame
from GameObject import GameObject
import Input
import Settings
from Text import Text

background_color = (100,100,255)
board_color = (0,255,0)
board_color2 = (100,255,100)

board_rect = pygame.Rect(20, 120, Settings.board_size[0] * Settings.cell_size[0], Settings.board_size[1] * Settings.cell_size[1])

class GameScene:
    def __init__(self):
        pass
    def update(self, delta_time):
        pass
    def render(self, gameDisplay):
        self.render_UIs(gameDisplay)
        
    def render_UIs(self, gameDisplay):
        pygame.draw.rect(gameDisplay, background_color, pygame.Rect(0, 0, Settings.display_width, Settings.display_height))
        for i in range(Settings.board_size[1]):
            for j in range(Settings.board_size[0]):
                rect = pygame.Rect(board_rect.left + j * Settings.cell_size[0], board_rect.top + i * Settings.cell_size[1], Settings.cell_size[0], Settings.cell_size[1])
                if (i+j)%2 == 0:
                    pygame.draw.rect(gameDisplay, board_color, rect)
                else:
                    pygame.draw.rect(gameDisplay, board_color2, rect)