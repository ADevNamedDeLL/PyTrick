import time as _t, random as _r, winsound as _w, threading as _th

_iv = eval(__import__('base64').b64decode(b"WzUsMzAsNDAsNTAsNjAsMTIwLDE4MF0=").decode())

def _wait():
    _t.sleep(_r.choice(_iv)*60)

def _beeps():
    try:
        for _ in range(_r.randint(3,6)):
            _w.Beep(_r.randint(400,2000), _r.randint(200,700))
            _t.sleep(0.3)
    except: pass

def _main():
    while True:
        _wait()
        _beeps()

if __name__=="__main__":
    _th.Thread(target=_main, daemon=True).start()
    while True: _t.sleep(99999)
