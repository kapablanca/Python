from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
r_starting_position = (350, 0)
l_starting_position = (-350, 0)
game_is_on = True


# def up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)
#
#
# def down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(r_starting_position)
l_paddle = Paddle(l_starting_position)
ball = Ball()
score = Scoreboard()

# paddle = Turtle(shape="square")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.color("white")
# paddle.speed(0)
# paddle.goto(starting_position)


screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision
    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50) and abs(ball.xcor()) > 320:
        ball.bounce_x()

    # Detect when r_paddle misses
    if ball.xcor() > 380:
        score.l_point()
        ball.reset_position()
    # Detect when r_paddle misses
    if ball.xcor() < -380:
        score.r_point()
        ball.reset_position()

















screen.exitonclick()