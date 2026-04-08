import pyglet
from data.init import WINDOW_HEIGHT, WINDOW_WIDTH
from models.color import BLACK, WHITE  
from extensions.sprite import center_x, center_y, create_sprite

__game_name_label = pyglet.text.Label("ESCAPE",
    anchor_x="center", anchor_y="center", font_size=36,
    x=WINDOW_WIDTH // 2, y=WINDOW_HEIGHT // 2)

__start_btn = create_sprite(400, 160, BLACK)
__start_btn.x = WINDOW_WIDTH // 2 - 200
__start_btn.y = WINDOW_HEIGHT // 2 - 200

__start_btn_label = pyglet.text.Label(
    "Старт [Enter]", font_size=24,
    anchor_x="center", anchor_y="center",
    x=center_x(__start_btn),
    y=center_y(__start_btn))

# Функция для отрисовки меню
def menu_draw():
    __game_name_label.draw()
    __start_btn.draw()
    __start_btn_label.draw()
