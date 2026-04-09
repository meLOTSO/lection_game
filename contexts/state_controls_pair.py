from controls.presets.dialog_controls import dialog_controls
from controls.presets.lose_controls import lose_controls
from controls.presets.menu_controls import menu_controls
from controls.presets.puzzle_controls import puzzle_controls
from controls.presets.running_controls import running_controls
from controls.presets.win_controls import win_controls
from controls.extensions.view_control_info import view_controls_info_controls
from states.game_state import GameState
from controls.game_controls import ControlType

# Список управлений для каждого игрового состояния

state_controls_pair = {
    GameState.DIALOG: [dialog_controls, view_controls_info_controls],
    GameState.LOSE: [lose_controls, view_controls_info_controls],
    GameState.MENU: [menu_controls, view_controls_info_controls],
    GameState.PUZZLE: [puzzle_controls, view_controls_info_controls],
    GameState.RUNNING: [running_controls, view_controls_info_controls],
    GameState.WIN: [win_controls, view_controls_info_controls]
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

