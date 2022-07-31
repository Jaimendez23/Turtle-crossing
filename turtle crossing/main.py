import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


FINISH_LINE_Y = 280
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()
car = CarManager()


screen.listen()
screen.onkeypress(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()
    if player.ycor() > FINISH_LINE_Y:
        player.start_position()
        score.score()
        car.move_faster()

    for x in car.all_cars:
        if x.distance(player) < 20:
            score.game_over()
            game_is_on = False


screen.exitonclick()





