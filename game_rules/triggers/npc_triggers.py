from data.dialogs.nps_scripts import NPC_FIRST_DIALOG_SCRIPT, NPC_FIRST_DIALOG_END_SCRIPT, NPC_CREATED_KEY_SCRIPT, NPC_IS_CRAZY_SCRIPT
from models.dialog_manager import get_flag_value, trigger_script_per
from models.enitites.npc import NPC_NAME

trigger_script_per(NPC_NAME, NPC_FIRST_DIALOG_SCRIPT, "start", triggered=True)
trigger_script_per(NPC_NAME, NPC_FIRST_DIALOG_END_SCRIPT, "npc_talked", priority=1)
trigger_script_per(NPC_NAME, NPC_CREATED_KEY_SCRIPT, "create_key", priority=2)
trigger_script_per(NPC_NAME, NPC_IS_CRAZY_SCRIPT, "crazy", priority=3)

def npc_first_dialog_ended():
    if get_flag_value("npc_talked"):
        tri