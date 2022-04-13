import pygame
from pygame.constants import K_LEFT
from GameObject import BOARD_SIZE, GameObject
from GameObject import Apple
from pygame import Vector2
import Input
import Settings
import Globals
from Text import Text
from Snake import Snake

background_color = (150,150,255)
board_color = (50,255,50)
board_color2 = (150,255,150)

board_rect = pygame.Rect(20, 120, Settings.board_size[0] * Settings.cell_size[0], Settings.board_size[1] * Settings.cell_size[1])

move_interval = 0.1

initial_length = 4

class GameScene:
    def __init__(self):
        self.crown = GameObject("images/crown.png", Settings.display_width / 2 + 170, 50)
        self.crown.set_size((self.crown.size[0] / 2, self.crown.size[1] / 2))
        self.best_score_text = Text(str(Globals.best_score), 30, self.crown.x + 35 , 50)
        self.score = 0
        self.score_text = Text("0", 40, Settings.display_width / 2 , 40)

        self.apple=Apple()
        self.snake=Snake(initial_length)
        
        self.tick = 0

    def update(self, delta_time):
        self.tick += delta_time
        if self.tick >= move_interval:
            self.snake.move_snake()
            self.has_collided()
            self.out_of_range()
            self.tick -= move_interval

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

    def has_collided(self):
        if self.apple.pos==self.snake.body[0]:
            self.apple.random_spawn()
            self.snake.add_snake()

    def out_of_range(self):
        if not 0<=self.snake.body[0].x<BOARD_SIZE or not 0<=self.snake.body[0].y<BOARD_SIZE:
            pygame.quit()
              
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