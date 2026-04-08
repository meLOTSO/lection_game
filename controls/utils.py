from controls.control_type import ControlType

def create_controls_dict(on_key_press=None, update=None, on_text=None):
    controls = {
        ControlType.ON_KEY_PRESS: on_key_press,
        ControlType.ON_TEXT: on_text,
        ControlType.UPDATE: update
    }
    return controls

