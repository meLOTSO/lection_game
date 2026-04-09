from controls.game_controls import create_controls_data

def on_key_press(symbol, modifier):
    pass

def update(dt):
    pass

__controls = create_controls_data(on_key_press, update)

def get_lose_controls():
    return __controls

lose_controls_info = {
    "Enter": "Начать заново"
}