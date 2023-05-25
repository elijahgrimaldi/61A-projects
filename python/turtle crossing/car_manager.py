from turtle import Turtle
import random as ran
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10

    def create_car(self):
        new_car = Turtle("square")
        new_car.shape("square")
        new_car.penup()
        new_car.turtlesize(stretch_wid=1,stretch_len=2)
        new_car.color(ran.choice(COLORS))
        new_car.goto(300,ran.randint(-250,250))
        self.all_cars.append(new_car)
    def move_left(self):
        for car in self.all_cars:
            car.backward(self.STARTING_MOVE_DISTANCE)

    
