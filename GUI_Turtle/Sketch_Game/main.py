from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()

def draw_control(key,fun):
    screen.onkeypress(key=key,fun=fun)

def move_forward():
    tim.forward(10)

def move_backword():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


draw_control(key="w",fun=move_forward)
draw_control(key="s",fun=move_backword)
draw_control(key="a",fun=turn_left)
draw_control(key="d",fun=turn_right)
draw_control(key="c",fun=clear_screen)
screen.exitonclick()
