from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
POSITION = random.randint(-300, 300)


class CarManager:
    def __init__(self):
        self.all_turtles = []
        # for _ in range(6):

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            tim = Turtle()
            tim.shape('square')
            tim.shapesize(1, 2)
            tim.color(random.choice(COLORS))
            tim.penup()
            tim.goto(300, random.randint(-250, 250))
            self.all_turtles.append(tim)

    def move_cars(self):
        for turtles in self.all_turtles:
            turtles.penup()
            turtles.backward(STARTING_MOVE_DISTANCE)
