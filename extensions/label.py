from pyglet.text import Label

from models.color import WHITE

__labels = []
__font_size = 0
__color = WHITE

def create_multipline_label(font_size, color=WHITE):
    global __labels, __font_size, __color
    __labels.clear()
    __font_size = font_size
    __color = color
    return __labels

def append_label(text):
    label = Label(text, font_size=__font_size)
    __labels.append(label)

def apply_label_dist(dist):
    dy = __font_size + dist
    cy = 0
    for label in __labels[-1::-1]:
        label.y += cy
        cy += dy

def apply_x(x):
    for label in __labels:
        label.x = x

def apply_y(y):
    for label in __labels:
        label.y += y

def draw_multipline_label(multipline_label):
    for label in multipline_label:
        label.draw()

def get_multipline_label_width(multipline_label):
    max_width = 0
    for label in multipline_label:
        max_width = max(max_width, label.content_width)
    return max_width

def get_multipline_label_height(multipline_label):
    start = __labels[-1].y
    end = __labels[0].y + __labels[0].content_height
    return end - start