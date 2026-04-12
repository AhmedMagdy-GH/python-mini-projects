from turtle import Turtle

PADDLE_SPEED = 40

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.paddle = Turtle()
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.shape("square")
        self.goto(position)

    def go_up(self):
        if self.ycor() < 230:
            new_y = self.ycor() + PADDLE_SPEED
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -230:
            new_y = self.ycor() - PADDLE_SPEED
            self.goto(self.xcor(), new_y)