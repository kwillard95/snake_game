import turtle as t
from snake import Snake
from food import Food
import time

screen = t.Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


def start_game():
    snake = Snake(screen)
    snake.start_game()
    food = Food(screen)
    food.place_food()
    print(snake.snake_running)
    head_of_snake = snake.segments[0]
    game_on = True
    while game_on:
        time.sleep(0.05)
        screen.update()
        if snake.snake_running:
            snake.move()


start_game()

screen.exitonclick()
