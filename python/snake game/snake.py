from turtle import Turtle
move_distance = 20
positions = [(0,0),(0,-20),(0,-40)]
UP,DOWN,LEFT,RIGHT = 90,270,180,0
class Snake():
    def __init__(self,length):
        self.length = length
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
    def move(self):
        for segment_number in range(len(self.snake_body)-1,0,-1):
            new_x = self.snake_body[segment_number-1].xcor()
            new_y = self.snake_body[segment_number-1].ycor()
            self.snake_body[segment_number].goto(new_x,new_y)
        self.head.forward(move_distance)
    def create_snake(self):
            for position in positions:
                self.add_segment(position)
    def add_segment(self,position):
                tim = Turtle("square")
                tim.color("white")
                tim.penup()
                tim.goto(position)
                self.snake_body.append(tim)
    def extend(self):
        self.add_segment(self.snake_body[-2].position())
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT) 
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT) 