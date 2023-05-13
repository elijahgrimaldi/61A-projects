from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreL = 0
        self.scoreR = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.scoreL} Score {self.scoreR}", align=ALIGNMENT, font=FONT)

    def increaseL(self):
        self.scoreL += 1
        self.clear()
        self.update_scoreboard()
    def increaseR(self):
        self.scoreR += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="Center", font=FONT)
