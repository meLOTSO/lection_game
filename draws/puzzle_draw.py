import pyglet
from data.init import WINDOW_HEIGHT, WINDOW_WIDTH
from extensions.sprite import create_sprite, center_x, center_y, center_into
from models.color import BLACK_ALPHA_150
from models.puzzle_input import get_input

PUZZLE_FONT_SIZE = 36
PUZZLE_INPUT_FONT_SIZE = 48

# content div
puzzle_box = create_sprite(
    WINDOW_WIDTH - 200, WINDOW_HEIGHT - 200, BLACK_ALPHA_150)

center_into(puzzle_box)

# Заголовок
puzzle_label = pyglet.text.Label(
    "Введите пароль:", anchor_x="center", anchor_y="center",
    x=center_x(puzzle_box), 
    y=center_y(puzzle_box) + 50,
    font_size=PUZZLE_FONT_SIZE
)
# Ввод
puzzle_input_label = pyglet.text.Label(
    "", font_size=PUZZLE_INPUT_FONT_SIZE,
    anchor_x="center", anchor_y="center",
    x=center_x(puzzle_box),
    y=center_y(puzzle_box)
)

def set_input_label_info(text):
    puzzle_input_label.text = text

def puzzle_draw():
    puzzle_box.draw()
    puzzle_label.draw()
    puzzle_input_label.draw()