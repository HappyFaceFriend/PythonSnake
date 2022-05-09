
from pygame import Vector2

UP = Vector2(0, -1)
DOWN = Vector2(0, 1)
LEFT = Vector2(-1, 0)
RIGHT = Vector2(1, 0)

class SnakeAI:
    def __init__(self, snake, initial_apple_pos):
        self.command_list = []
        self.snake = snake
        self.apple_pos = initial_apple_pos
        pass

    def pre_movement(self): #called at each frame just before movement of snake
        pass

    def post_movement(self): #called at each frame right after movement of snake
        pass
    
    def pre_death(self): #called at the frame just before the death of snake
        pass

    def post_apple_collision(self, new_apple_pos): #called right after the snake eats an apple
        self.apple_pos = new_apple_pos
        pass

    def get_snake_state_at(self, delta_frames): #get snake's state after delta_frames.
        return {}

    #returns index of the command in command list that passes point in the future, -1 if it doesn't.
    def check_commands_pass_point(self, point):
        return -1

    #returns index of the command in command list that kills the snake in the future, -1 if it doesn't.
    def check_commands_death(self):
        return -1
    