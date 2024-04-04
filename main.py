from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

# create screen object and adjust attributes
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)  # want to manually update the screen animations

# create player object
player = Player()

# create scoreboard object
scoreboard = Scoreboard()

# create car manager object
car_manager = CarManager()

# listen for input from keyboard
screen.listen()
screen.onkeypress(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(.1)
    scoreboard.update_scoreboard()
    screen.update()  # update screen animations every .1 sec

    if random.randint(1, 7) == 1:
        car_manager.create_car()  # controls and randomizes the number of cars being created

    car_manager.move_cars()

    # if player crosses finish line, levels up, resets player, and increases speed of cars
    if player.ycor() > 280:
        scoreboard.level_up()
        player.reset()
        car_manager.increase_speed()

    # detect player collision with car
    for car in car_manager.cars:
        if player.distance(car) < 30:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
