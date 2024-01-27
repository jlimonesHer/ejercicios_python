import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for i in range(0, 361, 5):
    print(i)
    tim.speed(500)
    tim.left(5)
    tim.color(random_color())
    tim.circle(100)

screen = t.Screen()
screen.exitonclick()