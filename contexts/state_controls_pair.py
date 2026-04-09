from controls.types.dialog_controls import get_dialog_controls
from controls.types.lose_controls import get_lose_controls
from controls.types.menu_controls import get_menu_controls
from controls.types.puzzle_controls import get_puzzle_controls
from controls.types.running_controls import get_running_controls
from controls.types.win_controls import get_win_controls
from states.game_state import GameState, set_game_state
from models.control_info import apple_control_info
from controls.game_controls import ControlType

# Список управлений для каждого игрового состояния

state_controls_pair = {
    GameState.DIALOG: [get_dialog_controls()],
    GameState.LOSE: [get_lose_controls()],
    GameState.MENU: [get_menu_controls()],
    GameState.PUZZLE: [get_puzzle_controls()],
    GameState.RUNNING: [get_running_controls()],
    GameState.WIN: [get_win_controls()]
}

# Зарегистрированные управления
# (вызываются именно эти управления)

__update_collection = []
__on_key_press_collection = []
__on_text_collection = []

def clear_collections():
    __update_collection.clear()
    __on_key_press_collection.clear()
    __on_text_collection.clear()

# Регистрация упарвления

def set_controls(game_state):
    set_game_state(game_state)

    clear_collections()
    for controls in state_controls_pair[game_state]:
        on_key_press = controls[ControlType.ON_KEY_PRESS]
        update = controls[ControlType.UPDATE]
        on_text = controls[ControlType.ON_TEXT]
        if on_key_press != None:
            __on_key_press_collection.append(on_key_press)
        if update != None:
            __update_collection.append(update)
        if on_text != None:
            __on_text_collection.append(on_text)

    apple_control_info()

# Функции для запуска зарегистрированных управлений

def update(dt):
    for updt in __update_collection:
        updt(dt)

def on_key_press(symbol, modifier):
    for okp in __on_key_press_collection:
        okp(symbol, modifier)

def on_text(text):
    for otxt in __on_text_collection:
        otxt(text)

