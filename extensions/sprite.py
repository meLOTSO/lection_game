import pyglet

from data.init import WINDOW_HEIGHT, WINDOW_WIDTH

def create_sprite(width, height, color, name=None):
    img = pyglet.image.SolidColorImagePattern(color)
    texture = img.create_image(width, height)
    sprite = pyglet.sprite.Sprite(texture)
    if name != None:
        sprite.__str__ = name
    return sprite

def center_x(sprite):
    return sprite.x + sprite.width // 2

def center_y(sprite):
    return sprite.y + sprite.height // 2

def center_into(sprite, p_sprite=None):
    if p_sprite == None:
        sprite.x = WINDOW_WIDTH // 2 - sprite.width // 2
        sprite.y = WINDOW_HEIGHT // 2 - sprite.height // 2