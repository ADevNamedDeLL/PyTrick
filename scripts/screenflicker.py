import ctypes as _c, time as _t, random as _r, threading as _th, base64 as _b

_v = _b.b64decode(b'WzUsMzAsNDAsNTAsNjAsMTIwLDE4MF0=')
def _f():
 while 1:
  _t.sleep(_r.choice(eval(_v.decode())))
  h = _c.windll.user32.GetDC(0)
  _c.windll.gdi32.SetBkColor(h, 0x000000)
  _t.sleep(0.2)
  _c.windll.gdi32.SetBkColor(h, 0xFFFFFF)

_th.Thread(target=_f, daemon=True).start()
_t.sleep(99999)
