from controls.game_controls import create_controls_data
from pyglet.window import key
import models.puzzle_input as puzzle_input
from states.game_state import GameState

def on_key_press(symbol, modifier):
    if symbol == key.BACKSPACE: # стереть последний символ
        puzzle_input.backspace()

    if symbol in (key.ENTER, key.RETURN): # подтвердить ввод
        puzzle_input.submit()

    if symbol == key.DELETE: # стереть текст
        puzzle_input.reset()
    
    if symbol == key.TAB: # выход в состояние running
        from contexts.state_context import change_game_state
        change_game_state(GameState.RUNNING)

def on_text(text):
    # В pyglet сюда приходят символы с учётом раскладки/Shift.
    if text and text.isprintable():
        puzzle_input.append_text(text)

puzzle_controls = create_controls_data(
    on_key_press=on_key_press, 
    update=None, 
    on_text=on_text)

puzzle_controls_info = {
    "Enter": "Подтвердить",
    "Delete": "Стереть весь текст",
    "Backspace": "Стереть последний символ",
    "Tab": "Закрыть"
}