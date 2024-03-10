import turtle
turtle.register_shape("footballer.gif")
turtle.register_shape("football.gif")
GRAVITY = 0.001

class CustomTurtle(turtle.Turtle):
    def __init__(self, x, y, shape):
        super().__init__()
        self.penup()
        self.shape(shape)
        self.setpos(x, y)

    #collision method

class Player(CustomTurtle):
    def __init__(self, x, y):
        super().__init__(x = x, y = y, shape = "footballer.gif")



class Goalkeeper(CustomTurtle):
    def __init__(self, x, y):
        super().__init__(y = y, x = x, shape = "square")
        self.color("blue")
        self.shapesize(1, 5)




class Football(CustomTurtle):
    def __init__(self, x, y):
        super().__init__(y = y, x = x, shape = "football.gif")
        self.velocity = 0
    def move_gravity(self):
        self.velocity -= GRAVITY
        self.sety(self.ycor() + self.velocity)

