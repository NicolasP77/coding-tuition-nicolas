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

    def on_collision(self, football_velocity, football_direction, football_x, football_y, constant):
        football_velocity += constant
        angle = math.degrees(math.atan2(football_y - self.ycor(), football_x - self.xcor()))
        # print(angle)
        football_direction = (angle + 180) % 360
        # print(angle)
        # football_direction = angle
        return football_direction, football_velocity
    #collision method

class Player(CustomTurtle):
    def __init__(self, x, y, window_width, window_height):
        super().__init__(x = x, y = y, shape = "footballer.gif")
        self.window_width = window_width
        self.window_height = window_height
        self.jumping = False
        self.y_init = y

    def move_right(self):
        if self.xcor() < self.window_width // 2:
            self.setx(self.xcor() + 3)

    def move_left(self):
        if self.xcor() > self.window_width // -2:
            self.setx(self.xcor() - 3)

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
                self.sety(self.ycor() - 3)
            if self.ycor() < self.y_init:
                self.jumping = False








class Goalkeeper(CustomTurtle):
    def __init__(self, x, y, goal_width):
        super().__init__(y = y, x = x, shape = "square")
        self.color("blue")
        self.shapesize(1, 5)
        self.goal_width = goal_width
    def move(self):
        self.setx(self.xcor() + 0.5)
        if self.xcor() > self.goal_width // 2:
            self.setx(-self.goal_width // 2)







class Football(CustomTurtle):
    def __init__(self, x, y):
        super().__init__(y = y, x = x, shape = "football.gif")
        self.velocity = 0
        self.direction = 90
        self.saved = False
    def move_gravity(self, player, goalkeeper, window_height):
        if self.ycor() < -window_height // 2:
            self.sety(0)
            self.velocity = 0
        self.velocity -= GRAVITY
        self.sety(self.ycor() + self.velocity * math.sin(math.radians(self.direction)))
        self.setx(self.xcor() + self.velocity * math.cos(math.radians(self.direction)))

        if self.distance(player) < 50 and self.ycor() > player.ycor():
            self.direction, self.velocity = player.on_collision(self.velocity, self.direction, self.xcor(), self.ycor(), PLAYER)
        if self.distance(goalkeeper) < 40:
            #print(self.direction)
            self.direction, self.velocity = goalkeeper.on_collision(self.velocity, self.direction, self.xcor(), self.ycor(), PLAYER)
            #print("save")
            #print(self.direction)


    def goal_scored(self, goal_y, goal_width):
        if self.ycor() > goal_y and self.xcor() < goal_width // 2 and self.xcor() > -goal_width // 2:
            goal = True
        else:
            goal = False
        return goal

