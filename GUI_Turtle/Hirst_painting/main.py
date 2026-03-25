import turtle as t
import colorgram
from random import choice

tim = t.Turtle()
tim.hideturtle()
tim.speed("fastest")
t.colormode(255)

def extract_color(path, number_of_colors):
    colors = colorgram.extract(path,number_of_colors)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r,g,b)
        rgb_colors.append(new_color)
    return rgb_colors


def painting(number_of_rows):
    tim.penup()
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)
    colors = extract_color('painting.jpg',30)
    for _ in range(number_of_rows):
        for _ in range(number_of_rows):
            tim.pendown()
            tim.dot(20,choice(colors))
            tim.penup()
            tim.forward(50)
        tim.penup()
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(number_of_rows *50)
        tim.left(180)
        tim.pendown()

painting(10)
screen = t.Screen()
screen.exitonclick()