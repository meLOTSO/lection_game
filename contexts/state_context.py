import contexts.state_controls_pair as state_controls_pair
import contexts.state_draws_pair as state_draws_pair
import contexts.extensions_draw as extensions_draw
from states.game_state import GameState, set_game_state

# Сменя состояний игры

def change_game_state(game_state):
    set_game_state(game_state)
    state_controls_pair.set_controls(game_state)
    state_draws_pair.set_draw(game_state)

# Функции сокращения для смены состояний

def to_menu():
    change_game_state(GameState.MENU)

def to_running():
    change_game_state(GameState.RUNNING)

def to_dialog():
    change_game_state(GameState.DIALOG)

def to_puzzle():
    change_game_state(GameState.PUZZLE)

def to_lose():
    change_game_state(GameState.LOSE)

def to_win():
    change_game_state(GameState.WIN)

# Функции управления

def update(dt):
    state_controls_pair.update(dt)

def on_key_press(symbol, modifier):
    state_controls_pair.on_key_press(symbol, modifier)

def on_text(text):
    state_controls_pair.on_text(text)

# Функция для отрисовки

def draw():
    state_draws_pair.draw()
    extensions_draw.draw()