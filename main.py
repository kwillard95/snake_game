import turtle
import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
from constants import WINDOW_PADDING

game_on = True


def end_game():
    global game_on
    game_on = False


screen = t.Screen()


def set_screen():
    screen.clear()
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)
    screen.setup(600, 600)


def start_game():
    global game_on
    set_screen()
    window_width = (screen.window_width() / 2) - WINDOW_PADDING
    window_height = (screen.window_height() / 2) - WINDOW_PADDING
    snake = Snake(screen, window_width, window_height)
    snake.start_game()
    food = Food()
    scoreboard = Scoreboard(window_width, window_height)

    while game_on:
        time.sleep(0.05)
        screen.update()
        scoreboard.show_score()
        if snake.snake_running:
            snake.move()
            is_snake_eating = snake.segments[0].distance(food) <= 20
            snake.check_stop_snake()
            if not snake.snake_running:
                game_on = False
            if is_snake_eating:
                scoreboard.score += 1
                print("POINT ADDED ", scoreboard.score)
                scoreboard.show_score()
                snake.add_snake_segment()
                food.reposition_food()
                screen.update()
    return scoreboard.score


def restart_game(game_score):
    global game_on
    if not game_on:
        user_input = screen.textinput("Game Ended",
                                      f"The game has ended. You got a score of {game_score}. "
                                      f"Type 'restart' to play again or 'cancel' to end game.").lower()
        if user_input == 'restart':
            game_on = True
        else:
            screen.bye()


while turtle.getscreen():
    score = start_game()
    restart_game(score)

screen.listen()
screen.onkeypress(end_game, 'Escape')
screen.exitonclick()
