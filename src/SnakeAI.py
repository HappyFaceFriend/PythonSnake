
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
        self.go_random = False
        self.random_dirs = [UP, LEFT, DOWN, RIGHT]
        self.find_path_to_apple()

    def find_path_to_apple(self):
        target = (int(self.apple_pos.x), int(self.apple_pos.y))
        result = self.find_path_to(target)
        if result != None:
            self.go_random = False
            self.go_through_path(result)
        else:
            while self.random_dirs[0] != self.snake.last_dir:
                self.random_dirs = self.random_dirs[1:] + [self.random_dirs[0]]
            self.go_random = True

    def go_through_path(self, result):
        if result == None:
            return
        for i in range(len(result)-1):
            self.command_list.append(Vector2(result[i+1][0] - result[i][0], result[i+1][1] - result[i][1]))

    def find_path_to(self, target):
        width = [Settings.board_size[0]-1, 0]
        height = [Settings.board_size[1]-1, 0]
        for cell in self.snake.body:
            width = min(width[0], int(cell.x)), max(width[1], int(cell.x))
            height = min(height[0], int(cell.y)), max(height[1], int(cell.y))
        width = [min(width[0], target[0]), max(width[1], target[0])]
        height = [min(height[0], target[1]), max(height[1], target[1])]
        if width[0]-1 >= 0:
            width[0] = width[0] -1
        if width[1]+1 <= Settings.board_size[0]-1:
            width[1] = width[1] + 1
        if height[0]-1 >= 0:
            height[0] = height[0] -1
        if height[1]+1 <= Settings.board_size[1]-1:
            height[1] = height[1] + 1
        
        map = [[0 for i in range(height[0], height[1]+1)] for j in range(width[0], width[1]+1)]
        for cell in self.snake.body[1:]:
            map[int(cell.x) - width[0]][int(cell.y)-height[0]] = 1
        head = (int(self.snake.body[0].x) - width[0], int(self.snake.body[0].y) - height[0])
        target = (target[0] - width[0], target[1] - height[0])
        return AStar.aStar(map, head, target)

    def check_empty(self, pos):
        if not 0<=pos.x<board_size[0] or not 0<=pos.y<board_size[1]:
            return False
        for block in self.snake.body[1:]:
            if block == pos:
                return False
        return True

    def pre_movement(self): #called at each frame just before movement of snake
        if self.go_random:
            i = 0
            while not self.check_empty(self.snake.body[0] + self.random_dirs[0]) and i<4:
                self.random_dirs = self.random_dirs[1:] + [self.random_dirs[0]]
                i += 1
            self.command_list.append(self.random_dirs[0])
            

    def post_movement(self): #called at each frame right after movement of snake
        if self.go_random:
            self.find_path_to_apple()
        else:
            #만약 머리가 몸을 스쳐지나가려하면
            #한칸 띄고 가게 해야함
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