import copy

SUBSCRIBERS = []

def subscribe(callback):
    SUBSCRIBERS.append(callback)

def send(message):
    for sub in SUBSCRIBERS:
        sub(copy.deepcopy(message))
