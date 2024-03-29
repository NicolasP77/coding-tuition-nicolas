import turtle
import time
import math
turtle.register_shape("footballer.gif")
turtle.register_shape("football.gif")
GRAVITY = 0.001
PLAYER = 0.1

class CustomTurtle(turtle.Turtle):
    def __init__(self, x, y, shape):
        super().__init__()
        self.penup()
        self.shape(shape)
        self.setpos(x, y)

    #collision method e

class Player(CustomTurtle):
    def __init__(self, x, y, window_width, window_height):
        super().__init__(x = x, y = y, shape = "footballer.gif")
        self.window_width = window_width
        self.window_height = window_height
        self.jumping = False
        self.y_init = y

    def move_right(self):
        if self.xcor() < self.window_width // 2:
            self.setx(self.xcor() + 1)

    def move_left(self):
        if self.xcor() > self.window_width // -2:
            self.setx(self.xcor() - 1)

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.sety(self.window_height // 5)

    def fall_down(self):
        #print(f'jumping: {self.jumping}')
        if self.jumping:
            #print(f'height reached: {self.ycor() == self.window_height // 5}')
            #print(self.ycor())
           # print(self.window_height // 5)
            if self.ycor() > self.y_init:
                self.sety(self.ycor() - 10)
            if self.ycor() < self.y_init:
                self.jumping = False




    def on_collision(self, football_velocity, football_direction, football_x, football_y):
        football_velocity += PLAYER
        angle = math.degrees(math.atan2(football_y - self.ycor(), football_x - self.xcor()))
        print(angle)
        football_direction = (football_direction + angle) % 360
        football_direction = angle
        return football_direction, football_velocity



class Goalkeeper(CustomTurtle):
    def __init__(self, x, y):
        super().__init__(y = y, x = x, shape = "square")
        self.color("blue")
        self.shapesize(1, 5)




class Football(CustomTurtle):
    def __init__(self, x, y,):
        super().__init__(y = y, x = x, shape = "football.gif")
        self.velocity = 0
        self.direction = 0
    def move_gravity(self, player):
        self.velocity -= GRAVITY
        self.sety(self.ycor() + self.velocity)
        if self.distance(player) < 20:
            self.direction, self.velocity = player.on_collision(self.velocity, self.direction, self.xcor(), self.ycor())

