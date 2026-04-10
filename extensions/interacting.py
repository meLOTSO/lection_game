# Регистрация объектов с коллбеком при нажатии E рядом с объектом.
# object_id — стабильный ключ (например NPC_NAME для dialog_manager).

interacting_objects = {}

def append_interacting(obj, func):
    oid = str(obj)
    
    if oid in interacting_objects:
        interacting_objects[oid]["objects"].append(obj)
    else:
        interacting_objects[oid] = {
            "objects": [obj],
            "func": func,
        }

def apply_interact():
    from extensions.physics import check_collision
    from models.enitites.player import get_player

    player = get_player()
    for entry in interacting_objects.values():
        for obj in entry["objects"]:
            if check_collision(player, obj):
                func = entry["func"]
                func(obj)
