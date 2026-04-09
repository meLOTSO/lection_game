from controls.game_controls import create_controls_data

def on_key_press(symbol, modifier):
    pass

def update(dt):
    pass

win_controls = create_controls_data(on_key_press, update)

win_controls_info = {
    "Enter": "Начать снова"
}
