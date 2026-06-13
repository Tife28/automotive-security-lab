import threading,time

from ids import main as ids_main
from can_simulator import main as sim_main
from attacker import main as attacker_main
from logs.bus_logger import main as logger_main

threading.Thread(target=ids_main, daemon=True).start()
threading.Thread(target=logger_main, daemon=True).start()
threading.Thread(target=sim_main, daemon=True).start()
threading.Thread(target=attacker_main, daemon=True).start()

while True:
    time.sleep(1)
