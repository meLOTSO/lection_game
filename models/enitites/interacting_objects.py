# Регистрация объектов с коллбеком при нажатии E рядом с объектом.
# object_id — стабильный ключ (например NPC_NAME для dialog_manager).

__interacting_objects = {}


def add_inetracting_object(sprite, func, object_id=None):
    if func is None:
        raise ValueError("func обязателен: вызов при успешном взаимодействии")
    oid = object_id if object_id is not None else str(id(sprite))
    __interacting_objects[oid] = {
        "object": sprite,
        "func": func,
    }


def is_interacting(object_id):
    return object_id in __interacting_objects


def get_interacting_objects():
    return __interacting_objects


def try_interact():
    """Проверить коллизию игрока с зарегистрированными объектами; вызвать первый func."""
    from extensions.physics import check_collision
    from models.enitites.player import get_player

    player = get_player()
    for entry in __interacting_objects.values():
        if check_collision(player, entry["object"]):
            entry["func"]()
            return True
    return False
