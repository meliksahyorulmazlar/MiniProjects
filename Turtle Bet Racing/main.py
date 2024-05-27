import random
from turtle import Turtle,Screen


class TurtleRacing:
    def __init__(self):
        self.colors:list[str] = ["red","blue","green","pink","purple"]
        self.y_coordinates:list[int] = [80,40,0,-40,-80]
        self.turtles = []
        for color in self.colors:
            turtle = Turtle()
            turtle.penup()
            turtle.shape("turtle")
            turtle.color(color)
            self.turtles.append(turtle)

    def race(self):
        screen = Screen()
        screen.title("Turtle Race Betting")
        screen.screensize(800, 800)
        for color in self.colors:
            turtle = self.turtles[self.colors.index(color)]
            turtle.goto(-230, self.y_coordinates[self.colors.index(color)])
            turtle.setheading(0)
        user_bet = screen.textinput(title="What is your bet?", prompt="Which color turtle will win?")
        racing = True
        while racing:
            for turtle in self.turtles:
                if turtle.xcor()>230:
                    racing = False
                    if user_bet == turtle.pencolor():
                        screen.textinput(title="Result", prompt=f"{turtle.pencolor()} won the race!")
                    elif user_bet != turtle.pencolor():
                        screen.textinput(title="Result", prompt=f"{turtle.pencolor()} won the race unlucky!")
                else:
                    turtle.forward(random.randint(1, 20))
        screen.exitonclick()

if __name__ == "__main__":
    bet = TurtleRacing()
    bet.race()


