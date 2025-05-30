import time as _t, random as _r, pymsgbox as _m, threading as _th

_iv = eval(__import__('base64').b64decode(b"WzUsMzAsNDAsNTAsNjAsMTIwLDE4MF0=").decode())

def _wait():
    _t.sleep(_r.choice(_iv)*60)

def _alert():
    try:
        _m.alert(text="⚠ Unusual odor detected near your device.\nPlease check your surroundings.", title="Sensor Alert", button="OK")
    except: pass

def _main():
    while True:
        _wait()
        _alert()

if __name__=="__main__":
    _th.Thread(target=_main, daemon=True).start()
    while True: _t.sleep(99999)
