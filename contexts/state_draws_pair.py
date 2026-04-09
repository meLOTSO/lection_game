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
    GameState.DIALOG: [dialog_draw, running_draw],
    GameState.PUZZLE: [puzzle_draw, running_draw],
    GameState.LOSE: [lose_draw],
    GameState.WIN: [win_draw],
}

# Список функций отрисовок - зарегистрированные отрисовки
# (содержит функции для отрисовок)

__draws = []
__extensions_draw = []

def append_extension_draw(on_draw):
    __extensions_draw.append(on_draw)

def remove_extension_draw(on_draw):
    if on_draw in __extensions_draw:
        __extensions_draw.remove(on_draw)

# Регистрация отрисовки

def set_draw(game_state):
    global __draws
    __draws = state_draws_pair[game_state]

# Отрисовка 

def draw():
    for drw in __draws:
        drw()
    for ext_drw in __extensions_draw:
        ext_drw()