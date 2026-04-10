from extensions.sprite import create_sprite
from models.color import BROWN
from models.enitites.interacting_objects import add_interacting_object

PUZZLE_NAME = "puzzle"

puzzle = create_sprite(80, 50, BROWN, PUZZLE_NAME)
puzzle.x = 600
puzzle.y = 400

def puzzle_interact(obj):
    from contexts.state_context import to_puzzle
    to_puzzle()
    # диалоги прописать
    
add_interacting_object(puzzle, puzzle_interact)

def draw_puzzle():
    puzzle.draw()