import turtle as t
import time

HEADING_VALUES = {
    "right": 0,
    "left": 180,
    "up": 90,
    "down": 270
}


class Snake:
    def __init__(self, screen):
        self.game_running = False
        self.segments = []
        self.screen = screen

    def create_snake_segment(self):
        segment = t.Turtle(shape="square")
        segment.color("white")
        segment.penup()
        self.segments.append(segment)
        return segment

    def add_snake_segment(self):
        num_of_snakes = len(self.segments)
        if num_of_snakes > 0:
            segment = self.create_snake_segment()
            last_segment_index = num_of_snakes - 1
            last_turtle_pos = self.segments[last_segment_index].xcor()
            segment.setx(last_turtle_pos - 20)
        else:
            self.create_snake_segment()
        self.screen.update()

    def shift_snake(self, direction):
        def move():
            if not self.game_running:
                self.game_running = True
            start_range = len(self.segments) - 1
            while self.game_running:
                time.sleep(0.05)
                self.screen.update()
                for seg_num in range(start_range, 0, -1):
                    previous_seg = self.segments[seg_num - 1]
                    new_x = previous_seg.xcor()
                    new_y = previous_seg.ycor()
                    self.segments[seg_num].goto(new_x, new_y)
                first_segment = self.segments[0]
                first_segment.setheading(HEADING_VALUES[direction])
                first_segment.forward(20)

        return move

    def start_game(self):
        total_segments = 3
        for _ in range(1, total_segments + 1):
            self.add_snake_segment()

        self.screen.listen()
        self.screen.onkeyrelease(self.shift_snake("right"), "Right")
        self.screen.onkeyrelease(self.shift_snake("left"), "Left")
        self.screen.onkeyrelease(self.shift_snake("up"), "Up")
        self.screen.onkeyrelease(self.shift_snake("down"), "Down")
