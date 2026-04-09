from enum import Enum

class ControlType(Enum):
    ON_KEY_PRESS = 1
    ON_TEXT = 2
    UPDATE = 3

# __controls = {
#     ControlType.ON_KEY_PRESS: None,
#     ControlType.ON_TEXT: None,
#     ControlType.UPDATE: None
# }

def create_controls_data(on_key_press=None, update=None, on_text=None):
    controls = {
        ControlType.ON_KEY_PRESS: on_key_press,
        ControlType.ON_TEXT: on_text,
        ControlType.UPDATE: update
    }
    return controls