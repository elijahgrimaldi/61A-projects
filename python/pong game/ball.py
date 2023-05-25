from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speedy = 2
        self.speedx = 2

    def move(self):
        new_x = self.xcor() + self.speedx
        new_y = self.ycor() + self.speedy
        self.goto(new_x,new_y)

    def bouncey(self):
        self.speedy *= -1
    def bouncex(self):
        self.speedx *= -1
