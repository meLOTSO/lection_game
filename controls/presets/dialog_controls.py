from pyglet.window import key
from controls.game_controls import create_controls_data
from game_rules.dialog_rules import next_replic

def on_key_press(symbol, modifier):
    if symbol == key.SPACE:
        next_replic()

def update(dt):
    pass

dialog_controls = create_controls_data(on_key_press, update)

dialog_controls_info = {
    "Space": "Далее"
}
