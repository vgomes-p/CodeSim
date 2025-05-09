import time
import threading

remaining_time = 0
lock = threading.Lock()

def format_time(seconds):
	mins, secs = divmod(seconds, 60)
	hours, mins = divmod(mins, 60)
	return '{:02d}h:{:02d}m:{:02d}s'.format(hours, mins, secs)

def countdown(total_time):
	global remaining_time
	with lock:
		remaining_time = total_time
	while remaining_time > 0:
		time.sleep(1)
		with lock:
			remaining_time -= 1

def start_countdown(seconds):
	global remaining_time
	with lock:
		remaining_time = seconds
	thread = threading.Thread(target=countdown, args=(seconds,), daemon=True)
	thread.start()
	return thread

def get_remaining_time():
	with lock:
		return remaining_time