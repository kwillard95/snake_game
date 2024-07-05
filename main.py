import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from constants import WINDOW_PADDING


def set_screen(current_screen):
    current_screen.clear()
    current_screen.bgcolor("black")
    current_screen.title("My Snake Game")
    current_screen.tracer(0)
    current_screen.setup(600, 600)


def end_game():
    scoreboard.display_game_over()
    screen.ontimer(screen.bye, 5000)
    screen.listen()
    screen.onkeypress(screen.bye, 'Escape')


def start_game():
    set_screen(screen)
    snake = Snake(screen, window_width, window_height)
    snake.start_game()
    food = Food()
    game_on = True

    def game_loop():
        nonlocal game_on
        nonlocal food
        global scoreboard
        if game_on:
            screen.update()
            scoreboard.show_score()
            if snake.snake_running:
                snake.move()
                is_snake_eating = snake.segments[0].distance(food) <= 20
                if not snake.snake_running:
                    game_on = False
                if is_snake_eating:
                    scoreboard.current_score += 1
                    scoreboard.show_score()
                    snake.add_snake_segment()
                    food.reposition_food()
                    screen.update()
            screen.ontimer(game_loop, 50)
        else:
            scoreboard.display_round_over()
            screen.ontimer(create_restart_game(scoreboard), 2000)

    game_loop()


def create_restart_game(prev_scoreboard):
    def restart_game():
        user_input = screen.textinput(
            "Game Ended",
            f"The game has ended. You got a score of {prev_scoreboard.current_score}. "
            f"Type 'restart' to play again or 'cancel' to end game."
        )
        if user_input and user_input.lower() == 'restart':
            start_game()
        else:
            end_game()

    return restart_game


screen = t.Screen()
set_screen(screen)
window_width = (screen.window_width() / 2) - WINDOW_PADDING
window_height = (screen.window_height() / 2) - WINDOW_PADDING
scoreboard = Scoreboard(window_width, window_height)

start_game()
screen.mainloop()
