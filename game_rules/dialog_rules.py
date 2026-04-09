from data.dialogs.nps_scripts import NPC_FIRST_DIALOG_END_SCRIPT
from models.dialog import clear_dialog, set_dialog_author_and_text
from models.dialog_manager import trigger
from models.dialog_scripts import next_replic_data


def show_first_dialog_line():
    apply_replic(next_replic_data())
    trigger(NPC_FIRST_DIALOG_END_SCRIPT)

def next_replic():
    apply_replic(next_replic_data())

def apply_replic(replic_data):
    if replic_data is None:
        clear_dialog()
        from contexts.state_context import to_running

        to_running()
        return
    author, text = replic_data
    set_dialog_author_and_text(author, text)
