from controls.types.dialog_controls import get_dialog_controls
from controls.types.lose_controls import get_lose_controls
from controls.types.menu_controls import get_menu_controls
from controls.types.puzzle_controls import get_puzzle_controls
from controls.types.running_controls import get_running_controls
from controls.types.win_controls import get_win_controls
from states.game_state import GameState, set_game_state, get_game_state
from controls.game_controls import change_game_controls
from states.game_state import GameState

state_controls_pair = {
    GameState.DIALOG: get_dialog_controls(),
    GameState.LOSE: get_lose_controls(),
    GameState.MENU: get_menu_controls(),
    GameState.PUZZLE: get_puzzle_controls(),
    GameState.RUNNING: get_running_controls(),
    GameState.WIN: get_win_controls()
}

def set_controls(game_state):
    set_game_state(game_state)
    change_game_controls(state_controls_pair[game_state])

def get_state():
    return get_game_state()

def update_controls():
    change_game_controls(state_controls_pair[get_game_state()])


# Удобные функции-сокращения для частых переходов

def to_menu():
    set_controls(GameState.MENU)

def to_running():
    set_controls(GameState.RUNNING)

def to_dialog():
    set_controls(GameState.DIALOG)

def to_puzzle():
    set_controls(GameState.PUZZLE)

def to_lose():
    set_controls(GameState.LOSE)

def to_win():
    set_controls(GameState.WIN)
