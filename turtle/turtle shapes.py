from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("arrow")
timmy.color("")
for num in range(3,11):
    angle = 360/num
    stop = 0
    while stop<=360:
        timmy.right(angle)
        timmy.forward(100)
        stop+=angle
screen = Screen()
screen.exitonclick()