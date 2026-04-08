from pyglet.window import key
from extensions.sprite import create_sprite
from models.color import GREEN_LIGTH
from data.init import KEYS
from extensions.physics import check_boundaries

PLAYER_SPEED = 300
PLAYER_NAME = "my_name"

__player = create_sprite(40, 40, GREEN_LIGTH, PLAYER_NAME)
__player.x = 100
__player.y = 300

def get_player():
    return __player

def draw_player():
    __player.draw()

def update_player_moving(dt):
    old_x, old_y = __player.x, __player.y

    if KEYS[key.RIGHT]:
        __player.x += PLAYER_SPEED * dt
    elif KEYS[key.LEFT]: 
        __player.x -= PLAYER_SPEED * dt
    
    if check_boundaries(__player):
        __player.x = old_x
        __player.y = old_y

def interaction():
    from models.enitites.interacting_objects import try_interact

    return try_interact()