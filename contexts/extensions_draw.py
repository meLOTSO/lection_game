__extensions_draw = []

def append_extension_draw(on_draw):
    __extensions_draw.append(on_draw)

def remove_extension_draw(on_draw):
    if on_draw in __extensions_draw:
        __extensions_draw.remove(on_draw)

def draw():
    for ext_draw in __extensions_draw:
        ext_draw()