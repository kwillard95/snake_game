import turtle as t
from constants import FONT_STYLE


class Scoreboard(t.Turtle):
    def __init__(self, window_width, window_height):
        super().__init__()
        self.score = 0
        self.window_width = window_width
        self.window_height = window_height

        self.goto(0,window_height - 10)
        self.shape("blank")
        self.color("white")

    def show_score(self):
        self.clear()
        self.write(f"Total score: {self.score}",False, "center", FONT_STYLE)

    def display_game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", False, "center", FONT_STYLE)


