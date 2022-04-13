import pygame
from pygame.constants import K_LEFT
from GameObject import GameObject
from GameObject import Apple
from GameObject import Snake
from pygame import Vector2
import Input
import Settings
import Globals
from Text import Text

background_color = (150,150,255)
board_color = (50,255,50)
board_color2 = (150,255,150)

board_rect = pygame.Rect(20, 120, Settings.board_size[0] * Settings.cell_size[0], Settings.board_size[1] * Settings.cell_size[1])

class GameScene:
    def __init__(self):
        self.crown = GameObject("images/crown.png", Settings.display_width / 2 + 170, 50)
        self.crown.set_size((self.crown.size[0] / 2, self.crown.size[1] / 2))
        self.best_score_text = Text(str(Globals.best_score), 30, self.crown.x + 35 , 50)
        self.score = 0
        self.score_text = Text("0", 40, Settings.display_width / 2 , 40)

        self.apple=Apple()
        self.snake=Snake()
        pass

    def update(self, delta_time):
        self.snake.move_snake()
        if Input.is_key_down(pygame.K_SPACE):
            self.add_score(1)
        if Input.is_key_down(pygame.K_UP):
            if self.snake.dir.y!=1:
                self.snake.dir=Vector2(0,-1)
        if Input.is_key_down(pygame.K_DOWN):
            if self.snake.dir.y!=-1:
                self.snake.dir=Vector2(0,1)
        if Input.is_key_down(pygame.K_LEFT):
            if self.snake.dir.x!=1:
                self.snake.dir=Vector2(-1,0)
        if Input.is_key_down(pygame.K_RIGHT):
            if self.snake.dir.x!=-1:
                self.snake.dir=Vector2(1,0)
        pass

    def render(self, gameDisplay):
        self.render_backgrounds(gameDisplay)
        self.render_UIs(gameDisplay)
        self.apple.draw_apple()
        self.snake.draw_snake()

    def add_score(self, score):
        self.score += score
        self.score_text.text = str(self.score)

    def render_backgrounds(self, gameDisplay):
        pygame.draw.rect(gameDisplay, background_color, pygame.Rect(0, 0, Settings.display_width, Settings.display_height))
        for i in range(Settings.board_size[1]):
            for j in range(Settings.board_size[0]):
                rect = pygame.Rect(board_rect.left + j * Settings.cell_size[0], board_rect.top + i * Settings.cell_size[1], Settings.cell_size[0], Settings.cell_size[1])
                if (i+j)%2 == 0:
                    pygame.draw.rect(gameDisplay, board_color, rect)
                else:
                    pygame.draw.rect(gameDisplay, board_color2, rect)
    def render_UIs(self, gameDisplay):
        self.crown.render(gameDisplay)
        self.best_score_text.render(gameDisplay)
        self.score_text.render(gameDisplay)