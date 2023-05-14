from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "Center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level {self.level}", align=ALIGNMENT, font=FONT)
    
    def increase(self):
        self.level += 1
        self.update_scoreboard

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="Center", font=FONT)