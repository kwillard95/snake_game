import turtle as t
from constants import NUMBER_OF_STEPS, HEADING_VALUES


class Snake:
    def __init__(self, screen, window_width, window_height):
        self.snake_running = False
        # A bit of a hack to override check_stop_snake when the snake moves from right to left initially
        self.first_left = True
        self.segments = []
        self.screen = screen
        self.window_width = window_width
        self.window_height = window_height

    def create_snake_segment(self, position):
        segment = t.Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def add_snake_segment(self):
        num_of_snakes = len(self.segments)
        if num_of_snakes > 0:
            last_segment_index = num_of_snakes - 1
            last_turtle_pos = self.segments[last_segment_index].pos()
            if not self.snake_running:
                position = (last_turtle_pos[0] - NUMBER_OF_STEPS, last_turtle_pos[1])
                self.create_snake_segment(position)
            else:
                self.create_snake_segment(last_turtle_pos)
        else:
            self.create_snake_segment((0, 0))



    def check_stop_snake(self):
        head_of_snake_pos = self.segments[0].pos()
        if abs(head_of_snake_pos[0]) >= self.window_width or abs(head_of_snake_pos[1]) >= self.window_height:
            return True
        head_of_snake = self.segments[0]
        for seg_num in range(1, len(self.segments)):
            if self.segments[seg_num].distance(head_of_snake) < 10:
                # A hack to override the collision of snake with its tail when the first left is taken due to the nature
                # of how the snake moves
                if self.first_left and head_of_snake.heading() == HEADING_VALUES['left']:
                    self.first_left = False
                    return False
                return True

    def move(self):
        if self.check_stop_snake():
            self.snake_running = False
            return
        start_range = len(self.segments) - 1
        for seg_num in range(start_range, 0, -1):
            previous_seg = self.segments[seg_num - 1]
            new_x = previous_seg.xcor()
            new_y = previous_seg.ycor()
            self.segments[seg_num].goto(new_x, new_y)
        first_segment = self.segments[0]
        first_segment.forward(NUMBER_OF_STEPS)

    def up(self):
        head_of_snake = self.segments[0]
        if head_of_snake.heading() != HEADING_VALUES['down']:
            first_segment = self.segments[0]
            first_segment.setheading(HEADING_VALUES["up"])
        self.snake_running = True

    def down(self):
        head_of_snake = self.segments[0]
        if head_of_snake.heading() != HEADING_VALUES['up']:
            first_segment = self.segments[0]
            first_segment.setheading(HEADING_VALUES["down"])
        self.snake_running = True

    def left(self):
        head_of_snake = self.segments[0]
        if head_of_snake.heading() != HEADING_VALUES['right'] or not self.snake_running:
            first_segment = self.segments[0]
            first_segment.setheading(HEADING_VALUES["left"])
        self.snake_running = True

    def right(self):
        head_of_snake = self.segments[0]
        if head_of_snake.heading() != HEADING_VALUES['left']:
            first_segment = self.segments[0]
            first_segment.setheading(HEADING_VALUES["right"])
        self.snake_running = True

    def shift_snake(self, direction):
        if direction == 'right':
            return self.right
        elif direction == 'left':
            return self.left
        if direction == 'up':
            return self.up
        if direction == 'down':
            return self.down

    def start_game(self):
        total_segments = 3
        for _ in range(1, total_segments + 1):
            print(self.segments)
            self.add_snake_segment()

        self.screen.listen()
        self.screen.onkeyrelease(self.shift_snake('right'), "Right")
        self.screen.onkeyrelease(self.shift_snake('left'), "Left")
        self.screen.onkeyrelease(self.shift_snake('up'), "Up")
        self.screen.onkeyrelease(self.shift_snake('down'), "Down")
