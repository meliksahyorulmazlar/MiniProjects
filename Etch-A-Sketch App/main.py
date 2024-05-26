import random
from turtle import Turtle,Screen

def forward():
    turtle.forward(10)

def backwards():
    turtle.backward(10)

def left():
    turtle.left(90)


def right():
    turtle.right(90)


def clear():
    turtle.clear()
    turtle.penup()
    turtle.goto(0,0)
    turtle.setheading(0)
    turtle.pendown()

if __name__ == "__main__":
    turtle = Turtle()
    screen = Screen()
    screen.title("Etch-A-Sketch App")
    turtle.speed(0)
    screen.listen()

    screen.listen()
    screen.onkey(key="w",fun=forward)
    screen.onkey(key="a", fun=left)
    screen.onkey(key="s", fun=backwards)
    screen.onkey(key="d", fun=right)
    screen.onkey(key="c",fun=clear)






    screen.exitonclick()
