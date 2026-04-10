from draws.inventory_draw import draw_inventory
import contexts.extensions_draw as extensions_draw

__flag = False
def toggle_inventory_view():
    global __flag
    __flag = not __flag
    if __flag:
        extensions_draw.append_extension_draw(draw_inventory)
    else:
        extensions_draw.remove_extension_draw(draw_inventory)
