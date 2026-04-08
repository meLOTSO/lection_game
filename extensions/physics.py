from data.init import WINDOW_WIDTH, WINDOW_HEIGHT

def check_boundaries(sprite):
    left_or_down = sprite.x < 0 or sprite.y < 0
    right_or_up = sprite.x + sprite.width > WINDOW_WIDTH or \
        sprite.y + sprite.height > WINDOW_HEIGHT
    return left_or_down or right_or_up

def check_collision(sprite1, sprite2):
    collide_x = (sprite1.x < sprite2.x + sprite2.width) and \
                (sprite1.x + sprite1.width > sprite2.x)
    collide_y = (sprite1.y < sprite2.y + sprite2.height) and \
                (sprite1.y + sprite1.height > sprite2.y)
    return collide_x and collide_y    