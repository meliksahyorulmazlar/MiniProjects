from turtle import Turtle,Screen
import random


class TurtleBetting:
    def __init__(self):
        self.turtles = []
        self.screen = Screen()
        self.screen.title("Turtle Race Betting")
        self.create_turtles()
        self.race()

    def create_turtles(self):
        colors = ["yellow","blue","red","orange","pink"]
        y_coordinates = [-200,-100,0,100,200]
        for i in range(len(colors)):
            color = colors[i]
            coordinate = y_coordinates[i]
            turtle = Turtle("turtle")
            turtle.color(color)
            turtle.penup()
            self.turtles.append(turtle)
            turtle.goto(-230,coordinate)

    def race(self):
        user_bet = self.screen.textinput(title="Which color turtle will win?",prompt="Enter the color")
        racing = True
        while racing:
            for turtle in self.turtles:
                magnitude = random.randint(0,20)
                turtle.forward(magnitude)
                if turtle.xcor() > 230:
                    color = turtle.pencolor()
                    play_again = self.screen.textinput(title=f"Winner: {color} Your bet: {user_bet}",prompt="Do you want to play again? (y/n)")
                    if play_again[0].lower() == "y":
                        self.reset()
                    else:
                        self.screen.bye()


    def reset(self):
        for turtle in self.turtles:
            turtle.speed(0)
            turtle.hideturtle()
            turtle.goto(-230,turtle.ycor())
            turtle.showturtle()
        self.race()




tb = TurtleBetting()
tb.screen.exitonclick()

