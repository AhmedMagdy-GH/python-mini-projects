# from turtle import Turtle,Screen
# from random import choice
# tim = Turtle()
# tim.speed("fastest")
# tim.pensize(15) # or width
#
#
# turtle_colors = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
# def random_walk():
#     for _ in range(200):
#         color = choice(turtle_colors)
#         tim.color(color)
#         tim.forward(30)
#         angle = choice([0,90,180,270])
#         tim.setheading(angle)
#
# random_walk()
# screen = Screen()
# screen.exitonclick()
#
#


import turtle as t
from random import choice,randint

tim = t.Turtle()
tim.speed("fastest")
tim.pensize(15) # or width
t.colormode(255)

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    rand_color = (r,g,b)
    return rand_color

def random_walk():
    for _ in range(100):
        tim.color(random_color())
        tim.forward(30)
        angle = choice([0,90,180,270])
        tim.setheading(angle)

random_walk()
screen = t.Screen()
screen.exitonclick()