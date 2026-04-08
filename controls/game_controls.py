from controls.control_type import ControlType

__controls = {
    ControlType.ON_KEY_PRESS: None,
    ControlType.ON_TEXT: None,
    ControlType.UPDATE: None
}

def on_key_press(symbol, modifier):
    func = __controls[ControlType.ON_KEY_PRESS]
    if func != None:
        func(symbol, modifier)

def on_text(text):
    func = __controls[ControlType.ON_TEXT]
    if func != None:
        func(text)

def update(dt):
    func = __controls[ControlType.UPDATE]
    if func != None:
        func(dt)

def change_game_controls(controls):
    global __controls
    __controls = controls