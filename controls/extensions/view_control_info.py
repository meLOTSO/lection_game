from pyglet.window import key
from controls.game_controls import create_controls_data
from game_rules.control_info_rules import toggle_view_control_info

def on_key_press(symbol, modifiers):
    # Левый/правый Ctrl; F1 — запасной вариант (на части раскладок/окон Ctrl ловится нестабильно)
    if symbol in (key.LCTRL, key.RCTRL, key.F1):
        toggle_view_control_info()

view_controls_info_controls = create_controls_data(
    on_key_press=on_key_press
)

view_controls_info_controls_info = {
    "Ctrl / F1": "Показать/скрыть управление",
}
