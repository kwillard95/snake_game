import turtle as t
import random as r


class Food:
    def __init__(self, screen):
        self.food_runner = t.Turtle()
        self.food_position = None
        self.food_present = False
        self.screen = screen

        self.food_runner.penup()
        self.food_runner.color("red")

    def generate_random_coordinates(self):
        half_window_width = (self.screen.window_width() / 2) - 20
        half_window_height = (self.screen.window_height() / 2) - 20
        x_cor = r.uniform(half_window_width * -1, half_window_width)
        y_cor = r.uniform(half_window_height * -1, half_window_height)
        coordinates = (x_cor, y_cor)
        return coordinates

    @staticmethod
    def generate_random_time():
        return r.randint(3000, 10000)

    def remove_food(self):
        self.food_runner.clear()
        self.food_position = None
        self.food_present = False

    def place_food(self):
        if self.food_position is not None:
            self.remove_food()
        coordinates = self.generate_random_coordinates()
        self.food_runner.goto(coordinates)
        self.food_position = coordinates
        self.food_runner.dot(20, "red")
        self.screen.ontimer(self.place_food, self.generate_random_time())
