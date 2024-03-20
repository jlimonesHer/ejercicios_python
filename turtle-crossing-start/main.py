import time
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()

player = Player()
screen.onkey(player.move_player, "Up")
car_manager = CarManager()
scoreboard = Scoreboard()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            time.sleep(1)
            scoreboard.game_over()

        if player.ycor() > 250:
            scoreboard.level_pass()
            player.starting_position()
            car_manager.add_difficult()

        if scoreboard.level == 3:
            game_is_on = False
            time.sleep(1)
            scoreboard.you_win()
screen.exitonclick()

