import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from constants import WINDOW_PADDING


in_game_loop = True
screen = t.Screen()


def end_game():
    screen.bye()


def set_screen():
    screen.clear()
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)
    screen.setup(600, 600)


def start_game():
    set_screen()
    window_width = (screen.window_width() / 2) - WINDOW_PADDING
    window_height = (screen.window_height() / 2) - WINDOW_PADDING
    snake = Snake(screen, window_width, window_height)
    snake.start_game()
    food = Food()
    scoreboard = Scoreboard(window_width, window_height)
    game_on = True
    def game_loop():
        nonlocal game_on
        if game_on:
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
                    scoreboard.show_score()
                    snake.add_snake_segment()
                    food.reposition_food()
                    screen.update()
            screen.ontimer(game_loop, 50)
        else:
            scoreboard.display_game_over()
            screen.ontimer(create_restart_game(scoreboard), 2000)

    game_loop()


def create_restart_game(prev_scoreboard):
    def restart_game():
        user_input = screen.textinput(
            "Game Ended",
            f"The game has ended. You got a score of {prev_scoreboard.score}. "
            f"Type 'restart' to play again or 'cancel' to end game."
        )
        if user_input and user_input.lower() == 'restart':
            start_game()
        else:
            screen.bye()

    return restart_game


set_screen()
screen.listen()
screen.onkeypress(end_game, 'Escape')
start_game()
screen.mainloop()
