from models.inventory import inventory
from models.enitites.player import player, PLAYER_NAME

game_data = {
    "player": player,
    "inventory": inventory,
    "door_locked": True,
    "chest_locked": True,
    "npc_talked": False,
    "puzzle_passwd": "world",
    "player_name": PLAYER_NAME,
}
