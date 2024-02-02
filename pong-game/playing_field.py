from turtle import Turtle, Screen


class PlayingField:

    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.created_screen()
        self.turtle = Turtle()
        self.created_turtle()
        self.draw_dashed_line()

    def draw_dashed_line(self):
        for _ in range(13):
            self.turtle.pendown()
            self.turtle.forward(30)
            self.turtle.penup()
            self.turtle.forward(30)

    def created_screen(self):
        self.screen = Screen()
        self.screen.setup(width=1200, height=800)
        self.screen.bgcolor("black")

    def created_turtle(self):
        self.turtle.color("white")
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(0, 380)
        self.turtle.pensize(7)
        self.turtle.pendown()
        self.turtle.right(90)

    def exitonclick(self):
        self.screen.exitonclick()
