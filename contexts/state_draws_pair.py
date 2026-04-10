from states.game_state import GameState, get_game_state
from draws.dialog_draw import dialog_draw
from draws.lose_draw import lose_draw
from draws.menu_draw import menu_draw
from draws.puzzle_draw import puzzle_draw
from draws.running_draw import running_draw
from draws.win_draw import win_draw

# Зарегистрированные отрисовки

state_draws_pair = {
    GameState.MENU: [menu_draw],
    GameState.RUNNING: [running_draw],
    GameState.DIALOG: [running_draw, dialog_draw],
    GameState.PUZZLE: [running_draw, puzzle_draw],
    GameState.LOSE: [lose_draw],
    GameState.WIN: [win_draw],
}

# Список функций отрисовок - зарегистрированные отрисовки
# (содержит функции для отрисовок)

__draws = []

# Регистрация отрисовки

def set_draw(game_state):
    global __draws
    __draws = state_draws_pair[game_state]

# Отрисовка 

def draw():
    for drw in __draws:
        drw()