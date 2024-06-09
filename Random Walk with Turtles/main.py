import random
import turtle
from turtle import Turtle,Screen




class TurtleSimulation:

    def __init__(self):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.screen = Screen()
        self.screen.title("Random Walk")
        self.screen.screensize(canvwidth=600,canvheight=600)
        self.screen.bgcolor("black")
        self.simulate()





    def simulate(self):
        directions = [0,90,180,270]
        while True:
            color_chosen = (random.randint(0,255)/255,random.randint(0,255)/255,random.randint(0,255)/255)
            turtle.pencolor(color_chosen)
            turtle.hideturtle()
            direction_chosen = random.choice(directions)
            turtle.left(direction_chosen)
            turtle.pensize(5)
            turtle.forward(10)




ts = TurtleSimulation()