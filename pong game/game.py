from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
Rpaddle = Paddle((350,0))
Lpaddle = Paddle((-350,0))
ball = Ball()
score = Score()




screen.listen()
screen.onkey(Rpaddle.go_up,"Up")
screen.onkey(Rpaddle.go_down, "Down")
screen.onkey(Lpaddle.go_up,"w")
screen.onkey(Lpaddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncey()
    if ball.distance(Rpaddle) < 50 and ball.xcor() > 340:
        ball.bouncex()
    if ball.distance(Lpaddle) < 50 and ball.xcor() < -340:
        ball.bouncex()
    if ball.xcor() > 380:
        score.increaseL()
        ball.goto(0,0)
    elif ball.xcor() < -380:
        score.increaseR()
        ball.goto(0,0)
    if score.scoreR == 5 or score.scoreL == 5:
        game_is_on = False
        score.game_over()

screen.exitonclick()