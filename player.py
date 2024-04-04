from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.setposition(STARTING_POSITION)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE  # increases y coordinate by the move distance
        self.setposition(0, new_y)  # sets player at new position

    def reset(self):
        """ resets player to starting position"""
        self.setposition(STARTING_POSITION)

