import pyglet

from models.color import BLACK, BLACK_ALPHA_150
from models.control_info import get_control_info
import extensions.label as label
from extensions.sprite import create_sprite

FONT_SIZE = 16
LABEL_DIST = 20
POS_X = 20
POS_Y = 200
PADDING = 10

def draw_control_info():
    control_info = get_control_info()
    if not control_info:
        return
    mulipline_label = label.create_multipline_label(FONT_SIZE)
    for key, info in control_info.items():
        label.append_label(f"[{key}] {info}")
    label.apply_label_dist(LABEL_DIST)
    label.apply_x(POS_X + PADDING)
    label.apply_y(POS_Y + PADDING)
    
    width = int(label.get_multipline_label_width(mulipline_label)) + PADDING * 2
    height = int(label.get_multipline_label_height(mulipline_label)) + PADDING * 2
    box = create_sprite(width, height, BLACK_ALPHA_150)
    box.x = POS_X
    box.y = POS_Y
    box.draw()
    label.draw_multipline_label(mulipline_label)

