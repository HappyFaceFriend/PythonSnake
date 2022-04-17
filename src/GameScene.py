import pygame
from GameObject import GameObject
from pygame import Vector2
import Input
import Settings
import Globals
from Text import Text
from Snake import Snake
import random
import time


background_color = (150,150,255)
board_color = (50,255,50)
board_color2 = (150,255,150)

board_rect = pygame.Rect(20, 120, Settings.board_size[0] * Settings.cell_size[0], Settings.board_size[1] * Settings.cell_size[1])

move_interval = 0.1

initial_length = 4


def get_image_pos(board_pos):
    return (Settings.border_size + board_pos[0]*Settings.cell_size[0],
            Settings.topbar_height + Settings.border_size + board_pos[1]*Settings.cell_size[1])

class GameScene:
    def __init__(self):
        self.crown = GameObject("images/crown.png", Settings.display_width / 2 + 170, 50)
        self.crown.set_size((self.crown.size[0] / 2, self.crown.size[1] / 2))
        self.best_score_text = Text(str(Globals.best_score), 30, self.crown.pos.x + 35 , 50)
        self.score = 0
        self.score_text = Text("0", 40, Settings.display_width / 2 , 40)

        self.apple=GameObject("images/apple.png")
        self.apple_boardpos = Vector2(0,0)
        self.spawn_apple()
        self.snake=Snake(initial_length)
        
        self.tick = 0
        
        self.background_sound = pygame.mixer.Sound("sounds/I Need a Stack.mp3")
        self.bite_sound = pygame.mixer.Sound("sounds/Bite.wav")
        self.background_sound.play(-1)

    def update(self, delta_time):
        self.tick += delta_time
        if self.tick >= move_interval:
            self.snake.update()
            self.has_collided()
            self.tick -= move_interval

        if Input.is_key_down(pygame.K_UP):
            if self.snake.last_dir.y!=1:
                self.snake.dir=Vector2(0,-1)
        if Input.is_key_down(pygame.K_DOWN):
            if self.snake.last_dir.y!=-1:
                self.snake.dir=Vector2(0,1)
        if Input.is_key_down(pygame.K_LEFT):
            if self.snake.last_dir.x!=1:
                self.snake.dir=Vector2(-1,0)
        if Input.is_key_down(pygame.K_RIGHT):
            if self.snake.last_dir.x!=-1:
                self.snake.dir=Vector2(1,0)
        if Input.is_key_down(pygame.K_ESCAPE):
            self.pause_game()

    def spawn_apple(self):
        x = random.randint(0, Settings.board_size[0] -1)
        y = random.randint(0,Settings.board_size[1] -1)
        self.apple_boardpos = Vector2(x,y)
        self.apple.pos = get_image_pos((x,y))
        
      
    def has_collided(self):
        print(self.apple_boardpos, self.snake.body[0])
        if self.apple_boardpos == self.snake.body[0]:
            self.spawn_apple()
            self.snake.add_snake()
            self.bite_sound.play()
              
    def render(self, gameDisplay):
        self.render_backgrounds(gameDisplay)
        self.render_UIs(gameDisplay)
        self.apple.render(gameDisplay)
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

    def pause_game(self):
        self.background_sound.stop()
        Globals.paused=True
        from PauseScene import PauseScene
        Globals.current_scene=PauseScene()