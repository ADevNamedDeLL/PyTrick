import pyttsx3 as _s, time as _t, threading as _th, random as _r, base64 as _b

_phr = [
 b'WW91IGZvcmdvdCBzb21ldGhpbmc=', b'RGlkIHlvdSBzZWUgdGhhdD8=',
 b'U2VyaW91c2x5LCB3aG8gd2FzIGp1c3QgaGVyZT8=',
 b'Q2xvc2UgdGhlIGxpZ2h0cw=='
]
_tms = [3600, 7200, 14400, 21600]

def _f():
 e = _s.init()
 while 1:
  _t.sleep(_r.choice(_tms))
  m = _b.b64decode(_r.choice(_phr)).decode()
  e.say(m)
  e.runAndWait()

_th.Thread(target=_f, daemon=True).start()
_t.sleep(99999)
