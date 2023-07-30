import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)   #doesnt show animation

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()  #updates screen everytime game is on
    ball.move()

    #collision detection with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #dect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        print("made contact")

screen.exitonclick()
