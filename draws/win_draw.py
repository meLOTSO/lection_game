import pyglet
from data.init import WINDOW_WIDTH, WINDOW_HEIGHT

__win_label = pyglet.text.Label("YOU WIN!",
    anchor_x="center", anchor_y="center",
    x=WINDOW_WIDTH // 2, y=WINDOW_HEIGHT // 2,
    font_size=32)

def win_draw():
    __win_label.draw()