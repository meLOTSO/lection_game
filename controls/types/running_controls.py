from controls.utils import create_controls_dict
from models.player import update_player_moving

def on_key_press(symbol, modifier):
    pass

def update(dt):
    update_player_moving(dt)

__controls = create_controls_dict(
    on_key_press=on_key_press, 
    update=update)

def get_running_controls():
    return __controls

running_controls_info = {
    "A": "Идти влево",
    "D": "Идти вправо",
    "Space": "Прыжок",
    "E": "Взаимодействие"
}