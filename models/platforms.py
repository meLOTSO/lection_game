from extensions.sprite import create_sprite
from models.color import GRAY_STONE

__platforms = []

def draw_platforms():
    for platform in __platforms:
        platform.draw()

def create_platform(width, height):
    platform = create_sprite(width, height, GRAY_STONE)
    return platform

def append_platform(width, height):
    platform = create_platform(width, height)
    __platforms.append(platform)
