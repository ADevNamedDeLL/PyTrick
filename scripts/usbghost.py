import time as _t
import random as _r
import ctypes as _c
import base64 as _b
import wmi as _w

_i = eval(_b.b64decode(b'WzUsMzAsNDAsNTAsNjAsMTIwLDE4MF0=').decode())

def _pop(m):
    _c.windll.user32.MessageBoxW(0, m, "USB ALERT", 0x10 | 0x1)

def _usb_count(c):
    return len(c.Win32_USBHub())

def _run():
    c = _w.WMI()
    _last = _usb_count(c)
    while True:
        _t.sleep(_r.choice(_i) * 60)
        _cur = _usb_count(c)
        if _cur > _last:
            _pop("WARNING: Data corruption detected on USB device!")
        _last = _cur

if __name__=="__main__":
    _run()
