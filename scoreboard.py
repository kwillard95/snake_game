import turtle as t
from constants import FONT_STYLE, SPACE_BETWEEN_TEXT, WINDOW_PADDING


class Scoreboard(t.Turtle):
    def __init__(self, window_width, window_height):
        super().__init__()
        self.current_score = 0
        self.window_width = window_width
        self.window_height = window_height
        self.rounds = []

        self.shape("blank")
        self.color("white")
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(0, self.window_height - WINDOW_PADDING)
        self.write(f"Total score: {self.current_score}",False, "center", FONT_STYLE)

    def display_round_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", False, "center", FONT_STYLE)
        self.rounds.append(self.current_score)
        self.current_score = 0


    def display_game_over_countdown(self, seconds):
        def countdown():
            nonlocal seconds
            self.screen.clear()
            self.write(f"Window will close in {seconds}", False, "center", FONT_STYLE)
            seconds -= 1
        return countdown

    def display_game_over(self):
        self.clear()
        x_cor = 0
        y_cor = self.window_height * .25
        for round_idx in range(len(self.rounds)):
            self.goto(x_cor, y_cor)
            self.write(f"Round {round_idx + 1}: {self.rounds[round_idx]}", False, "center", FONT_STYLE)
            y_cor -= SPACE_BETWEEN_TEXT
        self.goto(x_cor, y_cor)
        self.write("Press Escape key to close window now.", False, "center", FONT_STYLE)
