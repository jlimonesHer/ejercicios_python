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

def random_direction():
    num = random.randint(1, 3)
    if num == 1:
        tim.left(90)
        tim.forward(30)
    elif num == 2:
        tim.right(90)
        tim.forward(30)
    else:
        tim.forward(30)

def random_speed():
    num = random.randint(1, 3)
    tim.speed(num)

def random_walk():
    tim.pensize(15)
    num  = random.randint(1, 3)
    if num == 1:
        tim.color(random_color())
    elif num == 2:
        random_direction()
    else:
        random_speed()

while 1:
    random_walk()