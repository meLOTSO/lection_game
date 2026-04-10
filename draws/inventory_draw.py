from models.color import BLACK_ALPHA_150
from models.inventory import get_inventory_items
from extensions.sprite import create_sprite
import extensions.label as label

FONT_SIZE = 16
LABEL_DIST = 20
POS_X = 20
POS_Y = 500
PADDING = 10

def draw_inventory():
    inventory = get_inventory_items()
    multipline_label = label.create_multipline_label(FONT_SIZE)
    label.append_label("Инвентарь")
    for item, count in inventory.items():
        label.append_label(f"{item}: {count}")
    label.apply_label_dist(LABEL_DIST)
    label.apply_x(POS_X + PADDING)
    label.apply_y(POS_Y + PADDING)
    
    width = int(label.get_multipline_label_width(multipline_label)) + PADDING * 2
    height = int(label.get_multipline_label_height(multipline_label)) + PADDING * 2
    box = create_sprite(width, height, BLACK_ALPHA_150)
    
    box.draw()
    label.draw_multipline_label(multipline_label)