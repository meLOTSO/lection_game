from models.dialog import clear_dialog, set_dialog_author_and_text
from models.dialog_scripts import next_replic_data


def show_first_dialog_line():
    """Показать первую реплику после set_script (индекс сброшен в -1)."""
    _apply_replic(next_replic_data())


def next_replic():
    """Следующая реплика по Enter в режиме диалога."""
    _apply_replic(next_replic_data())


def _apply_replic(replic_data):
    if replic_data is None:
        clear_dialog()
        from contexts.state_context import change_game_state
        from states.game_state import GameState

        change_game_state(GameState.RUNNING)
        return
    author, text = replic_data
    set_dialog_author_and_text(author, text)
