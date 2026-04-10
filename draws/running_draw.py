from models.enitites.loot_silver import draw_loot_silver
from models.enitites.npc import draw_npc
from models.enitites.player import draw_player
from models.platforms import draw_platforms
from models.enitites.puzzle import draw_puzzle


def running_draw():
    draw_platforms()
    draw_loot_silver()
    draw_npc()
    draw_puzzle()
    draw_player()