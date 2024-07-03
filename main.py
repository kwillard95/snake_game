import turtle as t
from snake import Snake

screen = t.Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


def start_game():
    snake = Snake(screen)
    snake.start_game()


start_game()

screen.exitonclick()
