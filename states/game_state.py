from enum import Enum
import extensions.events as events

class GameState(Enum):
    MENU = 1
    RUNNING = 2
    DIALOG = 3
    PUZZLE = 4
    LOSE = 5
    WIN = 6

__current_state = GameState.MENU

def set_game_state(new_state):
    global __current_state
    __current_state = new_state
    events.apply_event("on_set_game_state")

def get_game_state():
    return __current_state
