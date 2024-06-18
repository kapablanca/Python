import turtle
from turtle import Turtle, Screen
import random


tim = Turtle()
turtle.colormode(255)
tim.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def mind_the_gap(gap):
    for _ in range(int(360/ gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.right(gap)


mind_the_gap(30)



screen = Screen()
screen.exitonclick()