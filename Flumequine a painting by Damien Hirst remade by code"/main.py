import random

import colorgram
from turtle import Turtle,Screen

#https://www.masterworksfineart.com/acquire/inquire/id/W-7567#btn
#https://hypemuseum.jp/products/flumequine-damien-hirst
#A million dollar painting painted in python



rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    color = (color.rgb[0]/255,color.rgb[1]/255,color.rgb[2]/255)
    rgb_colors.append(color)




if __name__ == "__main__":
    turtle = Turtle()
    screen = Screen()
    screen.title("Flumequine,2007 a painting by Damien Hirst painted by using code")
    turtle.penup()
    turtle.hideturtle()
    x = -150
    y = -150
    for i in range(1, 101):
        if i % 10 == 0:
            turtle.goto(x,y)
            turtle.dot(20,random.choice(rgb_colors))
            y += 30
            x = -150 + (i % 10 * 30)
        else:
            turtle.goto(x,y)
            turtle.dot(20, random.choice(rgb_colors))
            x += 30


    screen.exitonclick()
