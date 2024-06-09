import random
from turtle import Turtle,Screen


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(random.randint(-280,280),random.randint(-280,280))

    def move(self):
        self.hideturtle()
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
        self.showturtle()


class Snake:
    def __init__(self):
        self.screen = Screen()
        self.screen.title("Nokia Snake")
        self.screen.bgcolor("black")
        self.screen.listen()
        self.screen.setup(height=600,width=600)
        self.play()



    def create(self):
        positions = [(0,0),(-20,0),(-40,0)]
        for position in positions:
            turtle = Turtle("square")
            turtle.color("green")
            turtle.penup()
            turtle.goto(position)

            self.turtles.append(turtle)

    def move(self):
        for i in range(len(self.turtles)-1,0,-1):
            turtle = self.turtles[i]
            x = self.turtles[i-1].xcor()
            y = self.turtles[i-1].ycor()
            turtle.goto(x,y)
        self.turtles[0].forward(20)

    def ahead(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].setheading(90)
    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)
    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)

    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)

    def extend(self):
        last = self.turtles[-1]
        x = last.xcor()
        y = last.ycor()
        new_turtle = Turtle("square")
        new_turtle.hideturtle()
        new_turtle.color("green")
        new_turtle.penup()
        new_turtle.goto(x,y)
        new_turtle.showturtle()
        self.turtles.append(new_turtle)
    def play(self):
        self.turtles = []
        self.create()
        self.game_works = True
        food = Food()
        while self.game_works:
            self.move()
            self.screen.onkey(fun=self.ahead,key="w")
            self.screen.onkey(fun=self.left, key="a")
            self.screen.onkey(fun=self.down, key="s")
            self.screen.onkey(fun=self.right, key="d")
            head = self.turtles[0]
            if head.distance(food) < 25:
                food.move()
                self.extend()
            if abs(head.xcor()) >= 300 or abs(head.ycor()) >= 300:
                self.game_works = False
            for turtle in self.turtles[1:]:
                if head.distance(turtle) <5:
                    self.game_works = False


        play_again = self.screen.textinput(title="Do you want to play again?",prompt="Yes or No")
        if play_again[0].lower() == "y":
            for turtle in self.turtles:
                turtle.hideturtle()
            food.hideturtle()
            new_snake = Snake()
        else:
            exit()




snake = Snake()
snake.play()
snake.screen.exitonclick()














