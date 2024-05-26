import random
from turtle import Turtle,Screen


if __name__ == "__main__":
    turtle = Turtle()
    screen = Screen()
    screen.title("Spirograph")
    turtle.speed(0)
    turtle.pendown()
    turtle.hideturtle()
    while True:
        random_color = (random.randint(0,255)/255,random.randint(0,255)/255,random.randint(0,255)/255)
        turtle.left(1)
        turtle.pencolor(random_color)
        turtle.circle(100)




    screen.exitonclick()
