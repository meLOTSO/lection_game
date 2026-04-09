# events = {
#     "event_name": [func...]
# }

__events = {}

def append_event(event_name, func):
    if event_name in __events:
        __events[event_name].append(func)
    else:
        __events[event_name] = [func]

def apply_event(event_name):
    if event_name in __events:
        for func in __events[event_name]:
            func()
