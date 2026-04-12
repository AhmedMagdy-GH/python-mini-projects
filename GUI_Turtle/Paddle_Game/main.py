from numbers import Number
from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

winning_score = int(screen.textinput(title ="Pong Game", prompt="Enter the number of score to win:"))
player1 = screen.textinput(title ="Pong Game", prompt="Enter your name (left of the board): ")
player2 = screen.textinput(title ="Pong Game", prompt="Enter your name (right of the board):")

r_paddle= Paddle((360,0))
l_paddle= Paddle((-360,0))

ball= Ball((0,0))

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


def middle_line():
    mid_line = Turtle()
    mid_line.hideturtle()
    mid_line.color("white")
    mid_line.penup()
    mid_line.goto(0, 300)
    mid_line.setheading(270)

    for _ in range(30):
        mid_line.pendown()
        mid_line.forward(20)
        mid_line.penup()
        mid_line.forward(20)
middle_line()

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detected collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detected collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() >330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    #Detected Right paddle misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # Detected Left paddle misses
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

    if scoreboard.l_score == winning_score:
        scoreboard.print_winner(player1)
        game_on = False

    if scoreboard.r_score == winning_score:
        scoreboard.print_winner(player2)
        game_on = False


screen.exitonclick()