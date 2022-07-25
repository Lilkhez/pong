from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_point = 0
        self.r_point = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.l_point, align="center", font=("Courier", 70, "bold"))
        self.goto(100, 200)
        self.write(arg=self.r_point, align="center", font=("Courier", 70, "bold"))

    def l_score(self):
        self.l_point += 1
        self.update_score()

    def r_score(self):
        self.r_point += 1
        self.update_score()
