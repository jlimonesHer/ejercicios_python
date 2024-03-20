from turtle import Turtle, Screen

FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write("Level: " + str(self.level), align="right", font=("Courier", 40, "normal"))

    def level_pass(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 40, "normal"))

    def you_win(self):
        self.goto(0, 0)
        self.write("You Win", align="center", font=("Courier", 40, "normal"))