# object_scripts_and_triggers = {
#     "obj_id": [
#         {
#             "script_name": "...",
#             "into_done": 0,
#             "priority": 0
#         }
#     ]
# }

# trigger_flags = {
#     "flag": True|False    
# }

# Когда игрок касается объекта - проверяем, нет ли с ним сценария

from models.dialog_scripts import contains_script, set_script

__object_scripts_and_triggers = {}
__trigger_flags = {}

def trigger_script_per(object_name, script_name, trigger_flag, priority=0, triggered=False):
    data = {
        "script_name": script_name, 
        "trigger_flag": trigger_flag, 
        "priority": priority
    }
    __object_scripts_and_triggers.setdefault(object_name, []).append(data)
    __trigger_flags.setdefault(trigger_flag, triggered)

def trigger(flag):
    if flag in __trigger_flags:
        __trigger_flags[flag] = True

def get_flag_value(object_name, flag):
    if object_name in __object_scripts_and_triggers \
                and flag in __object_scripts_and_triggers[object_name]:
        return __object_scripts_and_triggers[object_name][flag]
    return False

def get_triggered_script_name(object_name):
    best = None
    best_priority = -10**9

    for data in __object_scripts_and_triggers.get(object_name, []):
        flag = data["trigger_flag"]
        if __trigger_flags.get(flag, False) and data["priority"] > best_priority:
            best = data["script_name"]
            best_priority = data["priority"]

    return best

def set_triggered_script(object_name):
    script_name = get_triggered_script_name(object_name)
    if script_name and contains_script(script_name):
        set_script(script_name)
        return True
    return False
