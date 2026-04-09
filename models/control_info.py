from states.game_state import GameState
from controls.presets.dialog_controls import dialog_controls_info
from controls.presets.lose_controls import lose_controls_info
from controls.presets.menu_controls import menu_controls_info
from controls.presets.puzzle_controls import puzzle_controls_info
from controls.presets.running_controls import running_controls_info
from controls.presets.win_controls import win_controls_info

__controls_info = {
    GameState.DIALOG: dialog_controls_info,
    GameState.LOSE: lose_controls_info,
    GameState.MENU: menu_controls_info,
    GameState.PUZZLE: puzzle_controls_info,
    GameState.RUNNING: running_controls_info,
    GameState.WIN: win_controls_info
}

__control_info = {}

def get_control_info():
    return __control_info

def set_control_info(game_state):
    global __control_info
    # копия, чтобы не менять исходные словари пресетов при append/update
    __control_info = dict(__controls_info[game_state])

def append_control_info(control_info):
    global __control_info
    __control_info.update(control_info)

