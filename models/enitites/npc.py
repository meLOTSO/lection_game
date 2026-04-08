from extensions.sprite import create_sprite
from models.color import RED_LIGHT
from models.enitites.interacting_objects import add_inetracting_object

NPC_NAME = "npc"

__npc = create_sprite(20, 40, RED_LIGHT, NPC_NAME)

__npc.x = 500
__npc.y = 400


def _npc_interact():
    from contexts.state_context import change_game_state
    from game_rules.dialog_rules import show_first_dialog_line
    from models.dialog_manager import set_triggered_script
    from states.game_state import GameState

    if set_triggered_script(NPC_NAME):
        change_game_state(GameState.DIALOG)
        show_first_dialog_line()


add_inetracting_object(__npc, _npc_interact, object_id=NPC_NAME)


def get_npc():
    return __npc

def draw_npc():
    __npc.draw()
