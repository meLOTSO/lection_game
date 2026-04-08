from states.game_state import GameState, get_game_state
from controls.types.dialog_controls import dialog_controls_info
from controls.types.lose_controls import lose_controls_info
from controls.types.menu_controls import menu_controls_info
from controls.types.puzzle_controls import puzzle_controls_info
from controls.types.running_controls import running_controls_info
from controls.types.win_controls import win_controls_info

control_info = {
    GameState.DIALOG: dialog_controls_info,
    GameState.LOSE: lose_controls_info,
    GameState.MENU: menu_controls_info,
    GameState.PUZZLE: puzzle_controls_info,
    GameState.RUNNING: running_controls_info,
    GameState.WIN: win_controls_info
}

def get_current_game_info():
    return control_info[get_game_state()]
