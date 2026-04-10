import pyglet
from data.init import WINDOW_HEIGHT, WINDOW_WIDTH
from extensions.sprite import create_sprite, center_x, center_y, center_into
from models.color import BLACK
from models.puzzle_input import get_input

PUZZLE_FONT_SIZE = 36
PUZZLE_INPUT_FONT_SIZE = 48

__puzzle_box = create_sprite(
    WINDOW_WIDTH - 200, WINDOW_HEIGHT - 200, BLACK)

center_into(__puzzle_box)

__puzzle_label = pyglet.text.Label(
    "Введите пароль:", anchor_x="center", anchor_y="center",
    x=center_x(__puzzle_box), 
    y=center_y(__puzzle_box) + 50,
    font_size=PUZZLE_FONT_SIZE
)

__puzzle_input_label = pyglet.text.Label(
    "", font_size=PUZZLE_INPUT_FONT_SIZE,
    anchor_x="center", anchor_y="center",
    x=center_x(__puzzle_box),
    y=center_y(__puzzle_box)
)

def update_input_label_info(text):
    __puzzle_input_label.text = text

def puzzle_draw():
    __puzzle_box.draw()
    __puzzle_label.draw()
    __puzzle_input_label.draw()