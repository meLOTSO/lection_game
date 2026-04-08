from contexts.state_controls_pair import set_controls
from contexts.state_draws_pair import set_draw

# Сменя состояний игры
def change_game_state(game_state):
    set_controls(game_state)
    set_draw(game_state)
