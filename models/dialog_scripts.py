# dialog_scripts = {
#     "script_name": [
#         {"author": "...", "replic": "..."}
#     ]
# }

__dialog_scripts = {}
__current_script = None
__replic_index = -1

# Создания сценария
def create_script(script_name):
    global __current_script
    __current_script = script_name
    __reproducible = True
    __dialog_scripts[script_name] = []

def get_current_script_name():
    return __current_script

# Задать сценарий
def set_script(script_name):
    global __current_script, __replic_index
    if script_name in __dialog_scripts:
        __replic_index = -1
        __current_script = script_name
    else:
        raise Exception(f"Не найден сценарий '{script_name}'")

# Создать объект {"author": "...", "replic": "..."}
def create_replic_data(author, replic):
    data = {
        "author": author,
        "replic": replic
    }
    return data

# Добавить реплику автора в сценарий
def append_replic(author, replic, script_name=None):
    if script_name is None:
        script_name = __current_script
    if script_name is None:
        raise Exception("Не задан сценарий для реплики")
    
    replic_data = create_replic_data(author, replic)
    __dialog_scripts[script_name].append(replic_data)

def get_replics_count(script_name=None):
    if script_name is None:
        script_name = __current_script
    if script_name in __dialog_scripts:
        return len(__dialog_scripts[script_name])
    else:
        return 0

def reset_replic_index():
    global __replic_index
    __replic_index = -1

def next_replic_data():
    global __replic_index
    __replic_index += 1
    if __replic_index >= get_replics_count() or __current_script is None:
        reset_replic_index()
        return None
    item = __dialog_scripts[__current_script][__replic_index]
    return (item["author"], item["replic"])

def contains_script(script_name):
    return script_name in __dialog_scripts