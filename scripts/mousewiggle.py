import pyautogui as _pg, threading as _th, time as _t, random as _r, base64 as _b

_v = _b.b64decode(b'WzUsMTUsMjAsMzAsNjBd')
def _f():
 while 1:
  _t.sleep(_r.choice(eval(_v.decode())))
  x, y = _pg.position()
  for _ in range(10):
   _pg.moveTo(x+5, y)
   _t.sleep(0.1)
   _pg.moveTo(x-5, y)
   _t.sleep(0.1)

_th.Thread(target=_f, daemon=True).start()
_t.sleep(99999)
