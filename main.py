import math
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from border import Border

#Create a Scenery of game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Programate Snake's Game")
screen.tracer(0)

#Animation Move Snake
game_is_on = True

snake=Snake()
food=Food()
scoreboard=ScoreBoard()
border=Border()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:

    screen.update()
    snake.move_snake()

    #colission food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    #colission board
    if snake.head.xcor()>240 or snake.head.xcor()<-240:
        game_is_on = False
        scoreboard.game_over()
    if snake.head.ycor()>240 or snake.head.ycor()<-240:
        game_is_on = False
        scoreboard.game_over()
    for segment in snake.snake_segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_is_on = False
            scoreboard.game_over()
    if len(snake.snake_segments)>576:
        game_is_on=False
        scoreboard.game_win()
    
    if len(snake.snake_segments)>1 and len(snake.snake_segments)<=100:
        time.sleep(0.2536*math.exp(-0.006392*len(snake.snake_segments)))

    if len(snake.snake_segments)>100 and len(snake.snake_segments)<=200:
        time.sleep(0.1721*math.exp(-0.003849*len(snake.snake_segments)))
    
    if len(snake.snake_segments)>200:
        time.sleep(0.079/len(snake.snake_segments))

screen.exitonclick()