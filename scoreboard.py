from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.level = 1

    def update_scoreboard(self):
        self.clear()
        self.setposition(-200, 245)
        self.write(f"LEVEL: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

