from pyglet.window import key
from controls.utils import create_controls_dict
from states.game_state import GameState

def on_key_press(symbol, modifier):
    if symbol == key.ENTER:
        from contexts.state_context import change_game_state

        change_game_state(GameState.RUNNING)

__controls = create_controls_dict(
    on_key_press=on_key_press)

def get_menu_controls():
    return __controls

menu_controls_info = {
    "Enter": "Начать"
}