import turtle
from turtle import Turtle, Screen
import random

# tem = Turtle(shape="turtle")
# tim = Turtle(shape="turtle")
# tom = Turtle(shape="turtle")
# tum = Turtle(shape="turtle")

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "green", "yellow", "blue", "purple"]
y_position = [-100, -50, 0, 50, 100]
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
all_turtles = []

for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-240, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"you`ve won! The {winning_color} turtle is the winner!")
            else:
                print(f"you`ve lost! The {winning_color} turtle is the winner!")

# tem.penup()
# tem.color("red")
# tem.goto(x=-240,y=50)
#
# tim.penup()
# tim.color("black")
# tim.goto(x=-240,y=100)
#
# tom.penup()
# tom.color("yellow")
# tom.goto(x=-240,y=-50)
#
# tum.penup()
# tum.color("purple")
# tum.goto(x=-240,y=-100)


screen.exitonclick()