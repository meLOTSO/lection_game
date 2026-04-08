import pyglet
from data.init import WINDOW_WIDTH, WINDOW_HEIGHT, KEYS, FPS

# Окно — до импортов, которые создают спрайты/текстуры (нужен активный GL-контекст)
window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT)

from contexts.state_context import change_game_state
import controls.game_controls as controls
from contexts.state_draws_pair import draw
from states.game_state import GameState
import game_rules.puzzle_rules as puzzle_rules

# Игровые правила

puzzle_rules.add_puzzle_rules()

# Обновления

def update(dt):
    controls.update(dt)

pyglet.clock.schedule_interval(update, 1/FPS)

@window.event
def on_key_press(symbol, modifiers):
    controls.on_key_press(symbol, modifiers)

@window.event
def on_text(text):
    controls.on_text(text)

@window.event
def on_draw():
    window.clear()
    draw()

# После @window.event: иначе set_handler перезапишет on_key_press KeyStateHandler
window.push_handlers(KEYS)

# Запуск игры
change_game_state(GameState.PUZZLE)

pyglet.app.run()