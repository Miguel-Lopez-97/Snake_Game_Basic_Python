from tkinter import LEFT, RIGHT
from turtle import Turtle

#Snake body
STARTING_POSITION = [(0,0),(-20,0)]

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    #constructor class
    def __init__(self):
        #Stay snake position
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
        
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segment = Turtle("square")
        snake_segment.color("#b0d12a")
        snake_segment.penup()
        snake_segment.goto(position)
        self.snake_segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def move_snake(self):
        for seg_num in range(len(self.snake_segments)-1,0,-1):

            new_x = self.snake_segments[seg_num-1].xcor()
            new_y = self.snake_segments[seg_num-1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)

        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)