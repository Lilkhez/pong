from turtle import Screen, Turtle
import turtle
from pad import Pad
from ball import Ball
import time
import random
from scoreboard import Scoreboard

tom = Turtle()
turtle.colormode(255)

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

ball = Ball()

board = Scoreboard()

pad1 = Pad()
pad2 = Pad()
pad2.goto(-350, 0)

screen.listen()
screen.onkeypress(pad1.up, "Up")
screen.onkeypress(pad1.down, "Down")

screen.onkeypress(pad2.up, "w")
screen.onkeypress(pad2.down, "s")

color_list = [
    (233, 225, 209), (216, 217, 222), (108, 110, 126), (209, 155, 98), (140, 141, 152), (186, 62, 31),
    (225, 213, 111), (233, 214, 224), (207, 148, 178), (102, 110, 172), (177, 157, 44), (222, 230, 223),
    (28, 27, 68), (29, 46, 28), (38, 41, 19), (194, 20, 7), (225, 169, 197), (209, 88, 63), (44, 46, 103),
    (234, 173, 160), (129, 80, 90), (157, 167, 159), (182, 184, 214), (84, 97, 85), (208, 80, 105),
    (183, 15, 22), (47, 28, 48), (70, 71, 42), (223, 205, 26), (52, 71, 54), (185, 197, 186), (120, 134, 120),
    (179, 196, 202), (113, 134, 141), (49, 68, 75)
]
game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with top and bottom and make it bounce
    if ball.ycor() > 290 or ball.ycor() < -280:
        ball.bounce()
        ball.color(random.choice(color_list))
    # Detect collision with the pads
    if ball.distance(pad1) < 50 and ball.xcor() > 320 or ball.distance(pad2) < 50 and ball.xcor() < -320:
        ball.pad_bounce()

    # Detect when ball misses the pads
    if ball.xcor() > 380:
        ball.reset_pos()
        board.l_score()

    if ball.xcor() < -380:
        ball.reset_pos()
        board.r_score()

screen.exitonclick()
