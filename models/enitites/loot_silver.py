"""Пример объекта с другим типом интерактива: добавление предмета в инвентарь."""

import models.inventory as inventory
from extensions.sprite import create_sprite
from models.color import SILVER
from models.enitites.interacting_objects import add_inetracting_object

LOOT_ID = "loot_silver"

__sprite = create_sprite(20, 20, SILVER)
__sprite.x = 250
__sprite.y = 360
__taken = False


def _take_silver():
    global __taken
    if __taken:
        return
    if inventory.append_item("silver", 1):
        __taken = True


add_inetracting_object(__sprite, _take_silver, object_id=LOOT_ID)


def draw_loot_silver():
    if not __taken:
        __sprite.draw()
