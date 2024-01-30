import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(198, 162, 101), (63, 90, 126), (139, 170, 191), (136, 91, 50), (132, 28, 53), (219, 205, 120), (29, 40, 65), (78, 16, 35), (149, 62, 85), (162, 155, 53), (184, 141, 158), (132, 182, 145), (48, 56, 99), (180, 97, 107), (56, 35, 22), (68, 130, 106), (98, 118, 166), (82, 148, 159), (221, 175, 187), (169, 206, 166), (90, 151, 96), (185, 97, 80), (163, 200, 213), (179, 188, 211), (80, 70, 39), (131, 37, 27)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots ):
    tim.pendown()
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

tim.dot(20, random.choice(color_list))

screen = turtle_module.Screen()
screen.exitonclick()