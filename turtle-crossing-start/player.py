STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200

from turtle import Turtle, Screen


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.shape("turtle")
        self.showturtle()
        self.left(90)
        self.starting_position()
        self.move_y = self.ycor()

    def starting_position(self):
        self.goto(STARTING_POSITION)

    def move_player(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
