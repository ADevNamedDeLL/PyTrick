import ctypes as _c, threading as _th, time as _t, random as _r, base64 as _b

_msgs = [
 b'UHJvY2Vzc29yIE92ZXJoZWF0OiBQb3dlclN1cmdlQWxlcnQ=', b'U3lzdGVtIEVycm9yOiBDU1YgY29ycnVwdGlvbg==',
 b'VXNlciBFcnJvcjogQWNjZXNzIGRlbmllZA==', b'TWVtb3J5IGFsbG9jYXRpb24gZmFpbGVk',
 b'SGFyZHdhcmUgUmVhZCBFcnJvcg=='
]
_tms = _b.b64decode(b'WzMsNSw4LDEyLDE1LDE4LDIwLDI1LDI4LDMwLDM1XQ==')
def _f():
 while 1:
  _t.sleep(_r.choice(eval(_tms.decode())))
  msg = _b.b64decode(_r.choice(_msgs)).decode()
  _c.windll.user32.MessageBoxW(0, msg, "System Alert", 0x10)

_th.Thread(target=_f, daemon=True).start()
_t.sleep(99999)
