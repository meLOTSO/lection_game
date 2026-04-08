from pyglet.window import key
from controls.utils import create_controls_dict
from game_rules.dialog_rules import next_replic

def on_key_press(symbol, modifier):
    if symbol == key.ENTER:
        next_replic()

def update(dt):
    pass

__controls = create_controls_dict(on_key_press, update)

def get_dialog_controls():
    return __controls

dialog_controls_info = {
    "Enter": "Далее"
}