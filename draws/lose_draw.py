import pyglet

from data.init import WINDOW_HEIGHT, WINDOW_WIDTH

__lose_label = pyglet.text.Label("YOU LOSE",
    anchor_x="center", anchor_y="center", font_size=36,
    x=WINDOW_WIDTH // 2, y=WINDOW_HEIGHT//2)

def lose_draw():
    __lose_label.draw()