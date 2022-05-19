import pygame
from GameObject import GameObject
from pygame import Vector2
from GameScene import GameScene
import Input
import Settings
import Globals
from Text import Text
from Snake import Snake
from GameOverScene import GameOverScene
import DataManager
import random
from SnakeAI import SnakeAI, UP, DOWN, LEFT, RIGHT


move_interval = 0.005

initial_length = 4

class AutoGameScene(GameScene):
    def __init__(self, state_dict = None):
        self.crown = GameObject("images/crown.png", Vector2(Settings.display_width / 2 + 170, 50))
        self.crown.set_size(self.crown.size[0] / 2, self.crown.size[1] / 2)
        best = DataManager.get_best_ranking()
        self.best_score_text = Text(str(0 if best is None else best[1]), 36, Vector2(self.crown.pos.x + 38 , 55))
        
        self.apple=GameObject("images/apple.png")
        if state_dict is None:
            self.apple_boardpos = Vector2(0,0)
            self.snake=Snake(initial_length)
            self.score = 0
            self.spawn_apple()
        else:
            self.apple_boardpos = Vector2(state_dict['apple_boardpos'][0],state_dict['apple_boardpos'][1])
            self.apple.pos = Vector2(state_dict['apple_pos'][0], state_dict['apple_pos'][1])
            self.snake = Snake(initial_length, state_dict['snake'])
            self.score = state_dict['score']
        
        self.score_text = Text(str(self.score), 50, Vector2(Settings.display_width / 2 , 50))
        self.tick = 0
        
        pygame.mixer.music.load("sounds/Banjo-Menu-Loop.wav")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        
        self.bite_sound = pygame.mixer.Sound("sounds/Bite.wav")
        self.bite_sound.set_volume(0.5)
        
        self.snake_ai = SnakeAI(self.snake, self.apple_boardpos)

    def update(self, delta_time):
        self.tick += delta_time
        if self.tick >= move_interval:
            self.snake_ai.pre_movement()
            if len(self.snake_ai.command_list)>0:
                self.snake.set_dir(self.snake_ai.command_list.pop(0))
                
            self.snake.update()
            if self.snake.is_dead:
                while(True):
                    pass
                self.on_gameover()
                
            self.check_apple_collision()
            self.snake_ai.post_movement()
            self.tick -= move_interval

            
        if Input.is_key_down(pygame.K_ESCAPE):
            self.pause_game()

    def check_apple_collision(self):
        if self.apple_boardpos == self.snake.body[0]:
            self.spawn_apple()
            self.snake.add_snake()
            self.bite_sound.play()
            self.add_score(1)
            self.snake_ai.post_apple_collision(self.apple_boardpos)
              
    def pause_game(self):
        pygame.mixer.music.pause()
        
        from PauseScene import PauseScene
        Globals.change_scene(PauseScene(self, True))

    def on_gameover(self):
        Globals.change_scene(GameOverScene(self.score, True))
