import time as _t, random as _r, os as _o, pyautogui as _p, threading as _th

_iv = eval(__import__('base64').b64decode(b"WzUsMzAsNDAsNTAsNjAsMTIwLDE4MF0=").decode())

def _wait():
    _t.sleep(_r.choice(_iv)*60)

def _zoom():
    try:
        _o.system("start magnify")
        _t.sleep(2)
        for _ in range(3): _p.hotkey('win', '+'); _t.sleep(0.5)
        _t.sleep(3)
        for _ in range(3): _p.hotkey('win', '-'); _t.sleep(0.5)
        _o.system("taskkill /IM magnify.exe /F")
    except: pass

def _main():
    while True:
        _wait()
        _zoom()

if __name__=="__main__":
    _th.Thread(target=_main, daemon=True).start()
    while True: _t.sleep(99999)
