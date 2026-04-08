from controls.utils import create_controls_dict

def on_key_press(symbol, modifier):
    pass

def update(dt):
    pass

__controls = create_controls_dict(on_key_press, update)

def get_lose_controls():
    return __controls

lose_controls_info = {
    "Enter": "Начать заново"
}