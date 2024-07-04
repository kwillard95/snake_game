import turtle as t
from snake import Snake
from food import Food
import time

screen = t.Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

game_on = True


def end_game():
    global game_on
    game_on = False


def start_game():
    global game_on
    snake = Snake(screen)
    snake.start_game()
    food = Food()
    total_score = 0

    while game_on:
        time.sleep(0.05)
        screen.update()
        if snake.snake_running:
            snake.move()
            is_snake_eating = snake.segments[0].distance(food) <= 20
            if is_snake_eating:
                total_score += 1
                print("POINT ADDED ", total_score)
                snake.add_snake_segment()
                food.reposition_food()
                screen.update()


screen.listen()
screen.onkeypress(end_game, 'Escape')
start_game()
screen.exitonclick()



