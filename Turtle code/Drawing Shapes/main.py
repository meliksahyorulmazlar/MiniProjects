from turtle import Turtle,Screen


if __name__ == "__main__":
    turtle = Turtle()
    screen = Screen()
    screen.title("Drawing Shapes")
    turtle.speed(0)
    turtle.penup()
    turtle.hideturtle()
    turtle.right(90)
    turtle.forward(300)
    turtle.left(90)
    turtle.pendown()
    for i in range(3,1000):
        total_angles = (i-2) * 180
        interior_angle = total_angles/i

        for j in range(i):
            turtle.forward(10)
            turtle.left(180-interior_angle)



    screen.exitonclick()
