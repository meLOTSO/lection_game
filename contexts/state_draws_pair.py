from states.game_state import GameState
from draws.dialog_draw import dialog_draw
from draws.lose_draw import lose_draw
from draws.menu_draw import menu_draw
from draws.puzzle_draw import puzzle_draw
from draws.running_draw import running_draw
from draws.win_draw import win_draw

__draws = []

state_draws_pair = {
    GameState.MENU: [menu_draw],
    GameState.RUNNING: [running_draw],
    GameState.DIALOG: [dialog_draw, running_draw],
    GameState.PUZZLE: [puzzle_draw, running_draw],
    GameState.LOSE: [lose_draw],
    GameState.WIN: [win_draw],
}

def draw():
    for drw in __draws:
        drw()

def set_draw(game_state):
    global __draws
    __draws = state_draws_pair[game_state]