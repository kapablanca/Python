from turtle import Turtle

STEP = -20
SEGMENTS = 3
# X_COORDINATES = [*range(0, STEP*SEGMENTS, STEP)]
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.tail = self.snake[-1]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake.append(segment)

    def reset(self):
        for segment in self.snake:
            segment.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
        self.tail = self.snake[-1]

    def extend_snake(self):
        self.add_segment(self.tail.position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment - 1].xcor()
            new_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)



