import time as _t
import random as _r
import base64 as _b
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

_i = eval(_b.b64decode(b'WzUsMzAsNDAsNTAsNjAsMTIwLDE4MF0=').decode())

class V:
    def __init__(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.vol = cast(interface, POINTER(IAudioEndpointVolume))
    def get(self):
        try:
            return self.vol.GetMasterVolumeLevelScalar()
        except Exception:
            return 0.5  # default volume fallback
    def set(self, v):
        try:
            self.vol.SetMasterVolumeLevelScalar(v, None)
        except Exception:
            pass

def run():
    v = V()
    while True:
        _t.sleep(_r.choice(_i)*60)
        cur = v.get()
        adj = max(0.0, min(1.0, cur + _r.choice([-0.01, 0.01])))
        v.set(adj)
        if _r.random() < 0.1:
            v.set(_r.uniform(0.3, 0.7))

if __name__=="__main__":
    run()
