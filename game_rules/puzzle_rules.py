from contexts.state_context import change_game_state
from models.dialog import set_dialog_text_and_author
import models.puzzle_input as puzzle_input
from data.game_data import game_data
from draws.puzzle_draw import update_input_label_info
from states.game_state import GameState


def check_puzzle(text):
    if text == game_data["puzzle_passwd"]:
        game_data["chest_locked"] = False
        set_dialog_text_and_author("Сундук открыт! Здесь и вправду было 2 серебра.", game_data["player_name"])
        change_game_state(GameState.DIALOG)
    else:
        puzzle_input.reset()

def add_puzzle_rules():
    puzzle_input.on_update(update_input_label_info)
    puzzle_input.on_submit(check_puzzle)