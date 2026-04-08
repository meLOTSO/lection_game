from data.dialogs.nps_scripts import NPC_FIRST_DIALOG_SCRIPT, NPC_FIRST_DIALOG_END_SCRIPT, NPC_CREATED_KEY_SCRIPT, NPC_IS_CRAZY_SCRIPT
from models.dialog_manager import get_flag_value, trigger, trigger_script_per
from models.enitites.npc import NPC_NAME
import models.inventory as inventory

trigger_script_per(NPC_NAME, NPC_FIRST_DIALOG_SCRIPT, NPC_FIRST_DIALOG_SCRIPT, triggered=True)
trigger_script_per(NPC_NAME, NPC_FIRST_DIALOG_END_SCRIPT, NPC_FIRST_DIALOG_END_SCRIPT, priority=1)
trigger_script_per(NPC_NAME, NPC_CREATED_KEY_SCRIPT, NPC_CREATED_KEY_SCRIPT, priority=2)
trigger_script_per(NPC_NAME, NPC_IS_CRAZY_SCRIPT, NPC_IS_CRAZY_SCRIPT, priority=3)
