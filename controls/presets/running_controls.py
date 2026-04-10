from pyglet.window import key
from controls.game_controls import create_controls_data
import models.enitites.player as player
import extensions.interacting as interacting
import game_rules.inventory_rules as inventory_rules

def on_key_press(symbol, modifier):
    if symbol == key.E:
        interacting.apply_interact()
    elif symbol == key.TAB:
        inventory_rules.toggle_inventory_view()

def update(dt):
    player.update_player_moving(dt)

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
