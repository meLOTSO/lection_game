from contexts.state_context import to_dialog
from models.dialog import set_dialog_author_and_text
from models.dialog_manager import set_triggered_script
from data.game_data import game_data
from models.enitites.puzzle import PUZZLE_NAME
import models.puzzle_input as puzzle_input
import extensions.events as events
import draws.puzzle_draw as puzzle_draw

PUZZLE_PASSWORD = "world"

def check_puzzle():
    input_text = puzzle_input.get_input()
    if input_text == PUZZLE_PASSWORD:
        game_data["chest_locked"] = False
        set_triggered_script(PUZZLE_NAME)
        to_dialog()
    else:
        puzzle_input.reset()

def update_input_draw():
    input_text = puzzle_input.get_input()
    puzzle_draw.set_input_label_info(input_text)

events.append_event("on_input", update_input_draw)
events.append_event("on_submit", check_puzzle)
events.append_event("on_set_puzzle_game_state", puzzle_input.reset)
