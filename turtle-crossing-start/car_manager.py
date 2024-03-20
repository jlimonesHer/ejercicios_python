from turtle import Turtle, Screen
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_change = random.randint(1,6)
        if random_change == 1:
            new_car = Turtle("square")
            new_car.speed = MOVE_INCREMENT
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def add_difficult(self):
        for car in self.all_cars:
            car.speed += MOVE_INCREMENT
            car.backward(car.speed)
