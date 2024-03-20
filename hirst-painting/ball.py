from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.turtle = Turtle()
        self.create_ball()

    def create_ball(self):
        self.turtle.penup()
        self.turtle.color("white")
        self.turtle.shape("circle")
        self.turtle.shapesize(stretch_len=1, stretch_wid=1)

    def move(self):
        self.turtle.forward(5)




