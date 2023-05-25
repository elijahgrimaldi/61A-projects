import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = Scoreboard()
game_loop_count = 0
screen.listen()
screen.onkey(player.move,"Up")


game_is_on = True
while game_is_on:
    if player.ycor() == 290:
        car.STARTING_MOVE_DISTANCE += car.MOVE_INCREMENT
        scoreboard.increase()
        scoreboard.update_scoreboard()
        player.goto(0,-280)
    for curr_car in car.all_cars:
        if player.distance(curr_car) < 15:
            game_is_on = False
            scoreboard.game_over()
    if game_loop_count==6:
        car.create_car()
        game_loop_count=0
    car.move_left()
    time.sleep(0.1)
    screen.update()
    game_loop_count += 1

screen.exitonclick()