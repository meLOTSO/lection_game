from pyglet.window import key
from extensions.sprite import create_sprite
from models.color import GREEN_LIGTH
from data.init import KEYS
from extensions.physics import check_boundaries

PLAYER_SPEED = 300
PLAYER_NAME = "my_name"

player = create_sprite(40, 40, GREEN_LIGTH, PLAYER_NAME)
player.x = 100
player.y = 300

def get_player():
    return player

def draw_player():
    player.draw()

def update_player_moving(dt):
    old_x, old_y = player.x, player.y

    if KEYS[key.W]:
        player.y += PLAYER_SPEED * dt
    elif KEYS[key.S]:
        player.y -= PLAYER_SPEED * dt
    if KEYS[key.D]:
        player.x += PLAYER_SPEED * dt
    elif KEYS[key.A]: 
        player.x -= PLAYER_SPEED * dt
    
    if check_boundaries(player):
        player.x = old_x
        player.y = old_y
