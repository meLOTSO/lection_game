from data.dialogs.nps_scripts import NPC_CREATED_KEY_SCRIPT, NPC_IS_CRAZY_SCRIPT
from extensions.sprite import create_sprite
from models.color import RED_LIGHT
from models.dialog_manager import get_flag_value, trigger
import models.inventory as inventory
import extensions.interacting as interacting

NPC_NAME = "npc"

npc = create_sprite(20, 40, RED_LIGHT, NPC_NAME)

npc.x = 500
npc.y = 400

def npc_interact(obj):
    from contexts.state_context import change_game_state
    from game_rules.dialog_rules import show_first_dialog_line
    from models.dialog_manager import set_triggered_script
    from states.game_state import GameState

    if inventory.has_item("clay") and inventory.has_item("silver", 3):
        trigger(NPC_CREATED_KEY_SCRIPT)

    if set_triggered_script(NPC_NAME):
        change_game_state(GameState.DIALOG)
        show_first_dialog_line()
    
    if get_flag_value(NPC_NAME, NPC_CREATED_KEY_SCRIPT):
        trigger(NPC_IS_CRAZY_SCRIPT)

interacting.append_interacting(npc, npc_interact)

def draw_npc():
    npc.draw()
