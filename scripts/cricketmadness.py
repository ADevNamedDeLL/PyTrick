import random as _r
import time as _t
from playsound import playsound as _p
import base64 as _b
import threading as _th
import sys
import os

# Encoded list of durations
_durations_encoded = _b.b64decode("WzUsMTAsMTUsMjAsMjUsMzAsMzUsNDAsNDUsNTAsNTUsNjBd").decode()
_durations = eval(_durations_encoded)

# Relative sound path using sys._MEIPASS for bundled data
def _get_sound_path():
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, "cricket.mp3")
    return os.path.join(os.path.abspath("."), "cricket.mp3")

def _run():
    while True:
        _sel = _r.choice(_durations)
        _t.sleep(_sel * 60)
        try:
            _p(_get_sound_path())
        except:
            pass

if __name__ == "__main__":
    _th.Thread(target=_run, daemon=True).start()
    while True:
        _t.sleep(99999)
