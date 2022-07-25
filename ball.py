from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.move_speed = 0.1
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def pad_bounce(self):
        self.x_move *= -1

    def reset_pos(self):
        self.home()
        self.move_speed = 0.1
        self.pad_bounce()
