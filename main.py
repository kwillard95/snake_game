import turtle as t
import time

screen = t.Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

current_direction = ""

segments = []


# snake = t.Turtle(shape="square")
# snake.color("white")
# snake.penup()
# snake.shapesize(stretch_len=3)

def create_snake_segment():
    segment = t.Turtle(shape="square")
    segment.color("white")
    segment.penup()
    segments.append(segment)
    return segment


def create_and_place_snake_segment():
    num_of_snakes = len(segments)
    if num_of_snakes > 0:
        segment = create_snake_segment()
        last_segment_index = num_of_snakes - 1
        last_turtle_pos = segments[last_segment_index].xcor()
        segment.setx(last_turtle_pos - 20)
    else:
        create_snake_segment()
    screen.update()


HEADING_VALUES = {
    "right": 0,
    "left": 180,
    "up": 90,
    "down": 270
}

game_running = True


def shift_snake(direction):
    def move():
        start_range = len(segments) - 1
        while game_running:
            time.sleep(0.05)
            screen.update()
            for seg_num in range(start_range, 0, -1):
                previous_seg = segments[seg_num - 1]
                new_x = previous_seg.xcor()
                new_y = previous_seg.ycor()
                segments[seg_num].goto(new_x, new_y)
            first_segment = segments[0]
            first_segment.setheading(HEADING_VALUES[direction])
            first_segment.forward(10)
    return move


def move_snake(direction):
    def move():
        global current_direction
        if current_direction == direction:
            return

        for segment in screen.turtles():
            if direction == "right":
                segment.setheading(0)
            elif direction == "left":
                segment.setheading(180)
            elif direction == "up":
                segment.setheading(90)
            elif direction == "down":
                segment.setheading(270)
            current_direction = direction
        while True:
            for segment in screen.turtles():
                segment.forward(10)
                screen.update()

    return move


def start_game():
    total_segments = 3
    for _ in range(1, total_segments + 1):
        create_and_place_snake_segment()

    screen.listen()
    screen.onkeyrelease(shift_snake("right"), "Right")
    screen.onkeyrelease(shift_snake("left"), "Left")
    screen.onkeyrelease(shift_snake("up"), "Up")
    screen.onkeyrelease(shift_snake("down"), "Down")


start_game()

screen.exitonclick()
