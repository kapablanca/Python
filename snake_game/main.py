from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(n=0)

snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.increase_score()

    #Detect collision with wall
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        score.reset()
        snake.reset()
        # game_is_on = False
        # score.game_over()

    #Detect collision with tail.
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
            # game_is_on = False
            # score.game_over()
    #if head collides with any segment in the tail:
    #trigger game_over


screen.exitonclick()
