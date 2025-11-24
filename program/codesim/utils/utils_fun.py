import time as tm
import sys
import os
if os.name == 'nt':
    import msvcrt
else:
    import termios
    import tty

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def letterby(entry, end='\n'):
    cnt = 0
    while cnt <= len(entry):
        nw_str = entry[0:cnt]
        print(f'\r{nw_str}|', end='', flush=True)
        tm.sleep(.05)
        cnt += 1
    print(f'\r{entry} ', end=end, flush=True)

def press_enter():
    if os.name == 'nt':
        while True:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key == b'\r':
                    break
            tm.sleep(0.01)
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            while True:
                ch = sys.stdin.read(1)
                if ch == '\r' or ch == '\n':
                    break
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)