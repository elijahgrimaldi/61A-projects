from turtle import Turtle, Screen
import turtle as t
import random


timmy = Turtle()
t.colormode(255)
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def random_color():
    r,g,b=random.randint(0,255),random.randint(0,255),random.randint(0,255)
    return (r,g,b)
turn = [90,-90,0,180]
timmy.pensize(10)
walk = 0
timmy.speed("fast")
while walk <= 200:
    timmy.color(random_color())
    timmy.forward(20)
    timmy.right(random.choice(turn))
    walk+=1
screen = Screen()
screen.exitonclick()