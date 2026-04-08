__input = ""
__submitted = False
__on_update = None
__on_submit = None

def append_text(text):
    global __input
    if not __submitted:
        __input += text
        if __on_update != None:
            __on_update(__input)

def submit():
    global __submitted
    __submitted = True
    if __on_submit != None:
        __on_submit(__input)

def get_input():
    return __input

def backspace():
    global __input
    if not __submitted:
        __input = __input[:-1]
        if __on_update != None:
            __on_update(__input)

def reset():
    global __input, __submitted
    __input = ""
    __submitted = False
    if __on_update != None:
        __on_update(__input)

# События

def on_update(on_update):
    global __on_update
    if on_update != None:
        __on_update = on_update

def on_submit(on_submit):
    global __on_submit
    if on_submit != None:
        __on_submit = on_submit