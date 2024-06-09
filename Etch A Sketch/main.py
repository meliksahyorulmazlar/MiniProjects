from turtle import Screen,Turtle




class Sketch:
    def __init__(self):
        self.screen = Screen()
        self.screen.title("Etch-A Sketch App")
        self.turtle = Turtle()
        self.draw()

    def forward(self):
        self.turtle.forward(10)

    def back(self):
        self.turtle.left(180)
        self.turtle.forward(10)

    def left(self):
        self.turtle.left(90)
        self.turtle.forward(10)

    def right(self):
        self.turtle.right(90)
        self.turtle.forward(10)

    def clear(self):
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.goto(0,0)
        self.turtle.pendown()
        self.turtle.setheading(0)

    def draw(self):
        self.screen.listen()
        self.screen.onkey(self.forward,"w")
        self.screen.onkey(self.left, "a")
        self.screen.onkey(self.back, "s")
        self.screen.onkey(self.right, "d")
        self.screen.onkey(self.clear,"c")





sketch = Sketch()
sketch.screen.exitonclick()