
from pygame import Vector2
from Settings import board_size
import AStar
import Settings

UP = Vector2(0, -1)
DOWN = Vector2(0, 1)
LEFT = Vector2(-1, 0)
RIGHT = Vector2(1, 0)

#Only control snake with command_list! Don't modify snake itself
class SnakeAI:
    def __init__(self, snake, initial_apple_pos):
        self.command_list = []
        self.snake = snake
        self.apple_pos = initial_apple_pos
        self.find_path_to_apple()

    def find_path_to_apple(self):
        map = [[0 for i in range(Settings.board_size[0])] for j in range(Settings.board_size[1])]
        for cell in self.snake.body[1:]:
            map[int(cell.x)][int(cell.y)] = 1
        head = (int(self.snake.body[0].x), int(self.snake.body[0].y))
        target = (self.apple_pos.x, self.apple_pos.y)
        result = AStar.aStar(map, head, target)
        print(head, self.apple_pos)
        if result != None:
            for i in range(len(result)-1):
                self.command_list.append(Vector2(result[i+1][0] - result[i][0], result[i+1][1] - result[i][1]))

    def pre_movement(self): #called at each frame just before movement of snake
        pass

    def post_movement(self): #called at each frame right after movement of snake
        pass

    def post_apple_collision(self, new_apple_pos): #called right after the snake eats an apple
        self.apple_pos = new_apple_pos
        self.find_path_to_apple()

    def get_snake_bodies_until(self, delta_frames): #returns snake's body states until delta_frames
        body = list(self.snake.body)
        lastdir = self.snake.last_dir
        ate_apple = False
        bodies = [body]
        for i in range(delta_frames):
            if i < len(self.command_list):
                command = self.command_list[i]
            else:
                command = lastdir
            if not self.is_valid_dir(command, lastdir):
                command = lastdir
            newcell = body[0] + command
            if newcell == self.apple_pos and not ate_apple:
                body = [newcell] + body
                ate_apple = True
            else:
                body = [newcell] + body[:-1]
            lastdir = command
            bodies.append(list(body))
        return bodies

    def is_valid_dir(self, dir, last_dir):
        if dir == Vector2(0,-1) and last_dir.y == 1:
            return False
        if dir == Vector2(0,1) and last_dir.y == -1:
            return False
        if dir == Vector2(-1, 0) and last_dir.x == 1:
            return False
        if dir == Vector2(1, 0) and last_dir.x == -1:
            return False
        return True

    def check_death(self, body):
        if not 0<=body[0].x<board_size[0] or not 0<=body[0].y<board_size[1]:
            return True
        for block in body[1:]:
            if block == body[0]:
                return True
        return False