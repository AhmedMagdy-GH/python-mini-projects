from turtle import Turtle , Screen
from random import choice

tim = Turtle()
tim.speed(5)
tim.width(5)
tim.shape("turtle")
tim.color("red")

# def dash_line():
#     for _ in range(10):
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#         tim.pendown()
# dash_line()

shapes = {
    "triangle":3,
    "square": 4,
    "pentagon": 5,
    "hexagon": 6,
    "heptagon": 7,
    "octagon": 8,
    "nonagon": 9,
    "decagon": 10
}

colors= ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]


def shape(sides ,cols):
    for shap, side in shapes.items():

        color = choice(cols)
        angle =  360 / side
        tim.color("black")
        for _ in range(side):
            tim.forward(100)
            tim.right(angle)
            tim.color(color)

shape(sides =shapes,cols = colors)


screen = Screen()
screen.exitonclick()