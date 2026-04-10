# inv = {
#     "item_name": [item, item]
# }

inventory = dict()

def register_for_inventory(item_name):
    inventory[item_name] = []

def get_inventory_items():
    inv = dict()
    for key, value in inventory.items():
        if value > 0:
            inv[key] = value
    return inv

def get_items_count(item_name):
    if item_name in inventory:
        return len(inventory[item_name])
    else:
        return 0

def contains_item(item_name, count=1):
    return get_items_count(item_name) >= count

def append_item(obj):
    item_name = str(obj)
    if item_name in inventory:
        inventory[item_name].append(obj)

def clear_items(item_name):
    if item_name in inventory:
        inventory[item_name].clear()

def take_item(item_name):
    if contains_item(item_name):
        item = inventory.pop(item_name)
    return None

def reset_inventory():
    for item_name in inventory:
        inventory[item_name].clear()

