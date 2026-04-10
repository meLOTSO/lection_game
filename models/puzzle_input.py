import extensions.events as events

__input = ""
__submitted = False

def append_text(text):
    global __input
    if not __submitted:
        __input += text
        events.apply_event("on_input")

def submit():
    global __submitted
    __submitted = True
    events.apply_event("on_submit")

def get_input():
    return __input

def backspace():
    global __input
    if not __submitted:
        __input = __input[:-1]
        events.append_event("on_input")

def reset():
    global __input, __submitted
    __input = ""
    __submitted = False
    events.apply_event("on_input")
