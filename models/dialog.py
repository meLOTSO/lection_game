import pyglet
from data.init import WINDOW_WIDTH
from extensions.sprite import center_x, center_y, create_sprite
from models.color import BLACK

DIALOG_TEXT_FONT_SIZE = 24
DIALOG_AUTHOR_NAME_TEXT_SIZE = 18
DIALOG_BOX_MARGIN = 40
DIALOG_BOX_PADDING = 20
DIALOG_BOX_WIDTH = WINDOW_WIDTH - DIALOG_BOX_MARGIN * 2
DIALOG_BOX_HEIGHT = 100

# Диалоговое окно
dialog_box = create_sprite(DIALOG_BOX_WIDTH, DIALOG_BOX_HEIGHT, BLACK)
dialog_box.x = DIALOG_BOX_MARGIN
dialog_box.y = DIALOG_BOX_MARGIN

# Текст диалога
dialog_label = pyglet.text.Label("", 
    anchor_x="center", anchor_y="center", font_size=DIALOG_TEXT_FONT_SIZE,
    x=center_x(dialog_box), y=center_y(dialog_box))

# Автор диалога
dialog_author_label = pyglet.text.Label("",
    anchor_x="left", anchor_y="top", font_size=DIALOG_AUTHOR_NAME_TEXT_SIZE,
    x=dialog_box.x + DIALOG_BOX_PADDING, y=dialog_box.x + dialog_box.height - DIALOG_BOX_PADDING)

# Для установки текста диалога
def set_dialog_text(text):
    dialog_label.text = text

# Для установки автора диалога
def set_author(author):
    dialog_author_label.text = author

# Для установки и текста и автора
def set_dialog_author_and_text(author, text):
    set_dialog_text(text)
    set_author(author)

# Для очистки текста и автора диалога
def clear_dialog():
    dialog_label.text = ""
    dialog_author_label.text = ""
