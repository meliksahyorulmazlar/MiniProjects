import random
from turtle import Turtle,Screen


if __name__ == "__main__":
    turtle = Turtle()
    screen = Screen()
    screen.title("Random Walk (Drunkard's Walk)")
    turtle.speed(0)
    turtle.pendown()
    turtle.hideturtle()
    while True:
        random_color = (random.randint(0,255)/255,random.randint(0,255)/255,random.randint(0,255)/255)
        turtle.pencolor(random_color)
        random_direction = random.randint(0,360)
        turtle.left(random_direction)
        turtle.forward(10)



    screen.exitonclick()
