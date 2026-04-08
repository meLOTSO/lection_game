# Регистрация объектов с коллбеком при нажатии E рядом с объектом.
# object_id — стабильный ключ (например NPC_NAME для dialog_manager).

__interacting_objects = {}


def add_interacting_object(sprite, func):
    oid = str(sprite)
    if oid in __interacting_objects:
        __interacting_objects[oid]["objects"].append(sprite)
    __interacting_objects[oid] = {
        "objects": [sprite],
        "func": func,
    }

def is_interacting(object_id):
    return object_id in __interacting_objects

def get_interacting_objects():
    return __interacting_objects


def try_interact():
    from extensions.physics import check_collision
    from models.enitites.player import get_player

    player = get_player()
    for entry in __interacting_objects.values():
        for obj in entry["objects"]:
            if check_collision(player, obj):
                entry["func"](obj)
                return True
    return False
