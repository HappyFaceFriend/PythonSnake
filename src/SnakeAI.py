
from turtle import up
from pygame import Vector2
from Settings import board_size

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
        self.collision = False
        pass

    def pre_movement(self): #called at each frame just before movement of snake

        if self.apple_pos[0] < self.snake.body[0][0]: # 사과가 뱀보다 왼쪽에 위치한 경우 
            if self.snake.last_dir == LEFT:
               pass
            elif self.snake.last_dir == RIGHT:
                if self.apple_pos[1] > self.snake.body[0][1]:
                    self.command_list.append(DOWN) 
                else:
                    self.command_list.append(UP)
            elif self.snake.last_dir == UP or self.snake.last_dir == DOWN:
                self.command_list.append(LEFT) 

        elif self.apple_pos[0] > self.snake.body[0][0]: # 사과가 뱀보다 오른쪽에 위치한 경우
            if self.snake.last_dir == RIGHT:
               pass
            elif self.snake.last_dir == LEFT:
                if self.apple_pos[1] > self.snake.body[0][1]:
                    self.command_list.append(DOWN) 
                else:
                    self.command_list.append(UP)
            elif self.snake.last_dir == UP or self.snake.last_dir == DOWN:
                self.command_list.append(RIGHT) 

        elif self.apple_pos[0] == self.snake.body[0][0]:
            if self.apple_pos[1] > self.snake.body[0][1]:
                if self.snake.last_dir == UP:
                    if self.snake.body[0][0] < 20:
                        self.command_list.append(RIGHT)
                    else:
                        self.command_list.append(LEFT)
                else:
                    self.command_list.append(DOWN) 
            else:
                if self.snake.last_dir == DOWN:
                    if self.snake.body[0][0] < 20:
                        self.command_list.append(RIGHT)
                    else:
                        self.command_list.append(LEFT)
                else:
                    self.command_list.append(UP)
        bodies = self.get_snake_bodies_until(len(self.snake.body)//4)
        for body in bodies:
            for i in range(4, len(body)):
                if body[0][0] == body[i][0] and body[0][1] == body[i][1]:
                    self.collision = True
                    self.command_list.clear()
                    dir = (body[i][0] - body[i-1][0], body[i][1] - body[i-1][1])
                    self.command_list.append(Vector2(dir))
                    break
            if self.collision == True:
                self.collision = False
                break

    def post_movement(self):  # called at each frame right after movement of snake

        bodies = self.get_snake_bodies_until(len(self.snake.body)//4)
        for body in bodies:
            for i in range(4, len(body)):
                if body[0][0] == body[i][0] and body[0][1] == body[i][1]:
                    self.collision = True
                    self.command_list.clear()
                    dir = (body[i][0] - body[i-1][0], body[i][1] - body[i-1][1])
                    self.command_list.append(Vector2(dir))
                    break
            if self.collision == True:
                self.collision = False
                break

    def post_apple_collision(self, new_apple_pos): #called right after the snake eats an apple
        self.apple_pos = new_apple_pos
        
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