from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        dic = random.randint(1, 6)
        if dic == 1:
            car = Turtle()
            car.penup()
            car.shape("square")  # A turtle with shape square starts as 20 * 20 pixels.
            random_y =random.randint(-250, 250)
            car.goto(300, random_y)
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(car)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
