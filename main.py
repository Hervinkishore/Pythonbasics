from turtle import Screen,Turtle
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
scoreboard=Scoreboard()
snake=Snake()
food=Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food)<15:
        food.refresh()
        scoreboard.updatedscore()
        snake.extend()

    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-300 or snake.segments[0].ycor()>300 or snake.segments[0].ycor()<-280:
        game_on=False
    for segment in snake.segments[1:]:
        if segment== snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment)<10:
            game_on=False



scoreboard.gameover()


screen.exitonclick()
