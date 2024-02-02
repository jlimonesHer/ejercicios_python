from playing_field import PlayingField
from ball import Ball
from player import Player

screen = PlayingField()
ball = Ball()
player1 = Player()
ball.dx = 2
ball.dy = 2
play_ball = True
while play_ball:
    ball.move()

screen.exitonclick()
