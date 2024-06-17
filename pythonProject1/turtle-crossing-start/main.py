import random
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
score = Scoreboard()
screen.listen()
screen.onkey(fun=player.up, key='Up')

# TODO. player reset

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    # detect collision with car
    for cars in car.all_turtles:
        if cars.distance(player) < 20:
            game_is_on = False

    # detect successful crossing
    if player.ycor() > 300:
        player.restart()

screen.exitonclick()
