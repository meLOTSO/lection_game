from models.control_info import set_control_info, append_control_info
from contexts.state_draws_pair import append_extension_draw, remove_extension_draw
from states.game_state import get_game_state
from draws.control_info_draw import draw_control_info
import extensions.events as events

def apply_control_info():
    from controls.extensions.view_control_info import view_controls_info_controls_info
    set_control_info(get_game_state())
    append_control_info(view_controls_info_controls_info)

__flag = False
def toggle_view_control_info():
    global __flag
    __flag = not __flag
    if __flag:
        apply_control_info()
        append_extension_draw(draw_control_info)
    else:
        remove_extension_draw(draw_control_info)

events.append_event("on_set_game_state", apply_control_info)