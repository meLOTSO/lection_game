"""Пример объекта с другим типом интерактива: добавление предмета в инвентарь."""

import models.inventory as inventory
from extensions.sprite import create_sprite, set_random_pos
from models.color import SILVER
from models.enitites.interacting_objects import add_interacting_object

LOOT_NAME = "loot_silver"
__loot_silvers = []

def take_silver(obj):
    inventory.append_item("silver", 1)
    __loot_silvers.remove(obj)

for i in range(5):
    sprite = create_sprite(20, 20, SILVER, LOOT_NAME)
    add_interacting_object(sprite, take_silver)
    set_random_pos(sprite)
    __loot_silvers.append(sprite)

def draw_loot_silver():
    for silver in __loot_silvers:
        silver.draw()
