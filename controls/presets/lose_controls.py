from controls.game_controls import create_controls_data

def on_key_press(symbol, modifier):
    pass

def update(dt):
    pass

lose_controls = create_controls_data(on_key_press, update)

lose_controls_info = {
    "Enter": "Начать заново"
}