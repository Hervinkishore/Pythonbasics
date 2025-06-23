import time
from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("The Pong game")
screen.tracer(0)

lpaddle=Paddle(-390)
rpaddle=Paddle(380)
lscore=Scoreboard("blue",-100,275)
rscore=Scoreboard("red",100,275)
ball=Ball()
print(ball)


screen.listen()

screen.onkeypress(rpaddle.up,"o")
screen.onkeypress(rpaddle.down,"l")
screen.onkeypress(lpaddle.up,"w")
screen.onkeypress(lpaddle.down,"s")

gameon=True
while gameon:
    time.sleep(0.05)
    ball.move()
    screen.update()
    if ball.ycor()<=-280 or ball.ycor()>=280:
        ball.bouncey()
    if (ball.xcor()<=-380 and ball.distance(lpaddle)<=50) or  (ball.xcor()>=380 and ball.distance(rpaddle)<=50):
        ball.bouncex()
    if ball.xcor()<=-400:
        rscore.inc()
        ball.mothala()
    if ball.xcor()>=400:
        lscore.inc()
        ball.mothala()














screen.exitonclick()
