from playing_field import PlayingField
from ball import Ball
from player import Player
from turtle import Turtle
STARTING_POSITIONS1 = (-570, 0)
STARTING_POSITIONS2 = (570, 0)

screen = PlayingField()
ball = Ball()
player1 = Player(STARTING_POSITIONS1, "red")
player2 = Player(STARTING_POSITIONS2, "blue")
play_ball = True
# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.

is_play = True
while is_play:
    ball.move()
    ball.turtle.speed(2)
    if ball.turtle.xcor() == 600 or ball.turtle.xcor() == -600:
        is_play = False
    # for segment in player2.segments:
    #     if ball.turtle.distance(segment) < 25:
    #         ball.turtle.left(180)
    #         ball.turtle.forward(1)
screen.exitonclick()
