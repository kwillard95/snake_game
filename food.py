import turtle as t
import random as r
from constants import WINDOW_PADDING


class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.turtlesize(.5)
        self.goto(self.generate_random_coordinates()[0], self.generate_random_coordinates()[1])

    def generate_random_coordinates(self):
        half_window_width = (self.screen.window_width() / 2) - WINDOW_PADDING
        half_window_height = (self.screen.window_height() / 2) - WINDOW_PADDING
        x_cor = r.uniform(half_window_width * -1, half_window_width)
        y_cor = r.uniform(half_window_height * -1, half_window_height)
        coordinates = (x_cor, y_cor)
        return coordinates

    @staticmethod
    def generate_random_time():
        return r.randint(5000, 10000)

    def reposition_food(self):
        coordinates = self.generate_random_coordinates()
        self.goto(coordinates[0], coordinates[1])
