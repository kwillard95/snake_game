import turtle as t


class Scoreboard(t.Turtle):
    def __init__(self, window_width, window_height):
        super().__init__()
        self.score = 0
        self.window_width = window_width
        self.window_height = window_height

        self.setx(0)
        self.sety(window_height - 10)
        self.shape("blank")
        self.color("white")

    def show_score(self):
        self.clear()
        self.write(f"Total score: {self.score}",False, "center", ("Arial", 16, 'bold'))




