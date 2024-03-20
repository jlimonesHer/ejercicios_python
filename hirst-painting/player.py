from turtle import Turtle


class Player():

    def __init__(self, position, color):
        self.turtle = Turtle()
        self.turtle.shape("square")
        # self.turtle.hideturtle()
        self.turtle.goto(position)
        self.turtle.color(color)
        self.turtle.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        self.setheading(90)

    def down(self):
        self.setheading(270)
