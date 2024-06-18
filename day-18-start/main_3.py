import random
from turtle import Turtle, Screen
import turtle
# import colorgram

# colors = colorgram.extract("hirst_painting.jpg", 20)
# colors_tuples = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     rgb = (r, g, b)
#     colors_tuples.append(rgb)
#
# print(colors_tuples)

tim = Turtle()
turtle.colormode(255)
tim.speed(0)
tim.penup()
tim.hideturtle()

color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83),
              (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48),
              (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
print(tim.position())

y = -212.13
for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    y += 50
    tim.setposition(-212.13, -212.13)
    tim.sety(y)









screen = Screen()
screen.exitonclick()
