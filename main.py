import pyglet
from data.init import WINDOW_WIDTH, WINDOW_HEIGHT, KEYS, FPS

# Окно — до импортов, которые создают спрайты/текстуры (нужен активный GL-контекст)
window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT, resizable=False)
pyglet.gl.glClearColor(0.2, 0.3, 0.5, 1.0)

import models.inventory as inventory
import contexts.state_context as state_context
import game_rules.puzzle_rules as puzzle_rules
import game_rules.triggers.npc_triggers  # noqa: F401 — регистрация сценариев и триггеров NPC

inventory.add_inventory_items("silver", "clay", "key")
import models.enitites.loot_silver  # noqa: F401 — регистрация подбираемого объекта

# Игровые правила

puzzle_rules.add_puzzle_rules()

# Обновления

def update(dt):
    state_context.update(dt)

pyglet.clock.schedule_interval(update, 1/FPS)

@window.event
def on_key_press(symbol, modifier):
    state_context.on_key_press(symbol, modifier)

@window.event
def on_text(text):
    state_context.on_text(text)

@window.event
def on_draw():
    window.clear()
    state_context.draw()

# После @window.event: иначе set_handler перезапишет on_key_press KeyStateHandler
window.push_handlers(KEYS)

# Запуск игры

state_context.to_menu()

pyglet.app.run()