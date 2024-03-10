import turtle
from football_game_class import *
window = turtle.Screen()
window.tracer(0)
window.setup(0.3, 0.8)
width = window.window_width()
height = window.window_height()
goal = turtle.Turtle()
goal.hideturtle()
game_on = True
goal.pensize(15)
goal.color("red")
football = Football(0, 0)
player = Player(0, -height // 2.9)
goalkeeper = Goalkeeper(0, height//2.7)



#window.register_shape("footballer.gif")
#player.shape("footballer.gif")


# goal:
window.bgcolor("green")
goal.penup()
goal.sety(height//2.2)
goal.pendown()
goal.forward(width // 3)
goal.backward(2*(width//3))
goal.right(90)
goal.forward(width//9)
goal.penup()
goal.setx(goal.xcor() + 2*(width//3))
goal.pendown()
goal.backward(width//9)

#def setup_game():
    # goalkeeper:


#setup_game()
while game_on:
    football.move_gravity()
    window.update()