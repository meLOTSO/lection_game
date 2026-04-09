from controls.game_controls import create_controls_data

def on_key_press(symbol, modifier):
    pass

def update(dt):
    pass

__controls = create_controls_data(on_key_press, update)

def get_win_controls():
    return __controls

win_controls_info = {
    "Enter": "Начать снова"
}
