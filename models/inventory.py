import pyglet

from data.init import WINDOW_HEIGHT

__inventory = dict()

__label = pyglet.text.Label("Инвентарь:", anchor_x="left", anchor_y="top", x=50, y=WINDOW_HEIGHT-50, font_size=24)

def get_inventory():
    return __inventory

def add_inventory_items(*args):
    for item in args:
        __inventory[item] = 0

def get_inventory_items():
    inventory = dict()
    for key, value in __inventory.items():
        if value > 0:
            inventory[key] = value
    return inventory

def has_item(name, count=1):
    return __inventory.get(name, 0) >= count

def append_item(name, count=1):
    if name in __inventory:
        __inventory[name] += count
        return True
    return False

def get_item_count(name):
    __inventory.get(name, 0);

def remove_item(name):
    if name in __inventory:
        __inventory[name] = 0

def try_take_item(name, count=1):
    if name in __inventory and __inventory[name] >= count:
        __inventory[name] -= count
        return True
    return False

def take_item(name, count=1):
    if not try_take_item(name, count):
        remove_item(name)

def reset_inventory():
    for key in __inventory:
        __inventory[key] = 0

def draw_inventory():
    __label.draw()