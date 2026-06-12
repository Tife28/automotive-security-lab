import queue

# Global shared message bus
CAN_BUS = queue.Queue()


def send(message):
    CAN_BUS.put(message)


def receive():
    if not CAN_BUS.empty():
        return CAN_BUS.get()
    return None
