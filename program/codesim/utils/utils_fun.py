import os
import time as tm

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