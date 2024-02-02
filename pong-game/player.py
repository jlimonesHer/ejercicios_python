from turtle import Turtle

STARTING_POSITIONS1 = [(-570, 0), (-570, -20), (-570, 20)]
STARTING_POSITIONS2 = [(570, 0), (570, -20), (570, 20)]


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_player(STARTING_POSITIONS1, "red")
        self.create_player(STARTING_POSITIONS2, "blue")
        self.head = self.segments[0]

    def create_player(self, position, color):
        for position in position:
            self.add_segment(position, color)

    def add_segment(self, position, color):
        new_segment = Turtle(shape="square")
        new_segment.color(color)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
