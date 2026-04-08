import pyglet
from data.init import WINDOW_WIDTH
from extensions.sprite import center_x, center_y, create_sprite
from models.color import BLACK

DIALOG_TEXT_FONT_SIZE = 24
DIALOG_AUTHOR_NAME_TEXT_SIZE = 18
DIALOG_BOX_WIDTH = WINDOW_WIDTH - 40
DIALOG_BOX_HEIGHT = 100

# Диалоговое окно
__dialog_box = create_sprite(DIALOG_BOX_WIDTH, DIALOG_BOX_HEIGHT, BLACK)
__dialog_box.x = 20
__dialog_box.y = 20

# Текст диалога
__dialog_label = pyglet.text.Label("", 
    anchor_x="center", anchor_y="center", font_size=DIALOG_TEXT_FONT_SIZE,
    x=center_x(__dialog_box), y=center_y(__dialog_box))

# Автор диалога
__dialog_author_label = pyglet.text.Label("",
    anchor_x="left", anchor_y="top", font_size=DIALOG_AUTHOR_NAME_TEXT_SIZE,
    x=__dialog_box.x + 20, y=__dialog_box.x + __dialog_box.height - 20)

# Для отрисовки диалога (фон, текст, автор)
def draw_dialog():
    __dialog_box.draw()
    __dialog_label.draw()
    __dialog_author_label.draw()

# Для установки текста диалога
def set_dialog_text(text):
    __dialog_label.text = text

# Для установки автора диалога
def set_author(author):
    __dialog_author_label.text = author

# Для установки и текста и автора
def set_dialog_author_and_text(author, text):
    set_dialog_text(text)
    set_author(author)

# Для очистки текста и автора диалога
def clear_dialog():
    __dialog_label.text = ""
    __dialog_author_label.text = ""
