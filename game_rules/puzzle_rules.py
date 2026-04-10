from contexts.state_context import to_dialog
from models.dialog import set_dialog_author_and_text
from models.dialog_manager import set_triggered_script
import models.puzzle_input as puzzle_input
from data.game_data import game_data
from draws.puzzle_draw import update_input_label_info
from models.enitites.puzzle import PUZZLE_NAME

def check_puzzle(text):
    if text == game_data["puzzle_passwd"]:
        game_data["chest_locked"] = False
        set_triggered_script(PUZZLE_NAME)
        to_dialog()
    else:
        puzzle_input.reset()

def add_puzzle_rules():
    puzzle_input.on_update(update_input_label_info)
    puzzle_input.on_submit(check_puzzle)
