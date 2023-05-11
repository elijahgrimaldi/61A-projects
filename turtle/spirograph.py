from turtle import Turtle, Screen
import turtle as t
import random
timmy = Turtle()
t.colormode(255)
timmy.speed("fastest")
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def random_color():
    r,g,b=random.randint(0,255),random.randint(0,255),random.randint(0,255)
    return (r,g,b)
for n in range(150):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.right(360/150)




screen = Screen()
screen.exitonclick()