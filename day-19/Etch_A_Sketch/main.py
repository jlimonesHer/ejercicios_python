from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def move_top():
    tim.forward(10)
def move_bottom():
    tim.backward(10)

def clear_paint():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(key="w", fun=move_top)
screen.onkey(key="s", fun=move_bottom)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_paint)
screen.exitonclick()