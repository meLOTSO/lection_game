from models.inventory import get_inventory
from models.enitites.player import get_player

game_data = {
    "player": get_player(),
    "inventory": get_inventory(),
    "door_locked": True,
    "chest_locked": True,
    "npc_talked": False,
    "puzzle_passwd": "world",
}
