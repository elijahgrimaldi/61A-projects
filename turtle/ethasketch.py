from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
def turn_left():
    tim.left(5)
def turn_right():
    tim.right(5)
def move_forward():
    tim.forward(10)
def move_back():
    tim.back(10)

screen.listen()
screen.onkey(move_forward,"Up")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(move_back, "Down")
screen.exitonclick()