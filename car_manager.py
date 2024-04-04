from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = 5

    def create_car(self):
        car = Turtle("square")
        car.shapesize(stretch_len=2)
        car.setheading(180)  # facing to the left
        car.penup()
        car.color(random.choice(COLORS))  # assigns random color from COLORS
        y_cor = random.randint(-250, 250)
        car.setposition(300, y_cor)  # random position just out of view on right x-axis
        self.cars.append(car)  # adds car object to list of cars

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += 1

