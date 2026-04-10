from pyglet.window import key
from controls.game_controls import create_controls_data
from models.enitites.interacting_objects import try_interact
from models.enitites.player import update_player_moving
from game_rules.inventory_rules import toggle_inventory_view

def on_key_press(symbol, modifier):
    if symbol == key.E:
        try_interact()
    elif symbol == key.TAB:
        toggle_inventory_view()

def update(dt):
    update_player_moving(dt)

running_controls = create_controls_data(
    on_key_press=on_key_press, 
    update=update)

running_controls_info = {
    "A": "Идти влево",
    "D": "Идти вправо",
    "Space": "Прыжок",
    "E": "Взаимодействие",
    "Tab": "Показать/скрыть инвентарь",
}
