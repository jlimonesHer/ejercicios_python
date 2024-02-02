from turtle import Screen
import time
from snake import Snake
from foot import Foot
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
foot = Foot()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

play_game = True
while play_game:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(foot) < 15:
        foot.refresh()
        score.increase_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 \
        or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        play_game = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            play_game = False
            score.game_over()

screen.exitonclick()
