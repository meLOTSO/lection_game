"""Пример объекта с другим типом интерактива: добавление предмета в инвентарь."""

import models.inventory as inventory
from extensions.sprite import create_sprite, set_random_pos
from models.color import SILVER
import extensions.interacting as interacting

CLAY_NAME = "loot_silver"
clays = []

def take_clay(obj):
    inventory.append_item(obj)
    clays.remove(obj)

for i in range(5):
    clay = create_sprite(20, 20, SILVER, CLAY_NAME)
    interacting.append_interacting(clay, take_clay)
    set_random_pos(clay)
    clays.append(clay)

def draw_clays():
    for clay in clays:
        clay.draw()
