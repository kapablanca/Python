import turtle
from turtle import Turtle, Screen
import random



tim = Turtle()
tim.shape("turtle")
tim.color("green")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for i in range(3, 11):
    degrees = 360/i
    tim.color(random_color())
    for times in range(i):
        tim.forward(100)
        tim.right(degrees)










screen = Screen()
screen.exitonclick()
