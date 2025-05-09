import time as tm
from codesim.utils.database import add_user, get_user, user_exists
from codesim.utils.utils_fun import clear, letterby
from codesim.utils.countdown import format_time, start_countdown, get_remaining_time

CODESHELL = 'codeshell $> '
CREATESHELL = 'USER CREATOR $> '
SIMTEXT = f"""eval: evaluate
finish: end the exam
time: show much time rest
update: shows assigment, directory, assigment's score, time, number of try and points to receive"""

def simshell():
	while True:
		tm.sleep(1)
		letterby("Welcome to Code Exam Simulator!")
		tm.sleep(1)
		letterby("Please, inform your username!")
		tm.sleep(0.5)
		login = input("Login: ").strip()
		if not login:
			letterby("Username cannot be empty.")
			continue
		user = get_user(login)
		if user:
			print(f"Welcome back, {login}! {user['language']} coder at level {user['level']}...")
			language = user['language']
			level = user['level']
			break
		else:
			letterby(f"No user found for '{login}'. Creating a new user...")
			tm.sleep(0.5)
			while True:
				print("Which language do you study? (we have simulation for C and Python only!)")
				tm.sleep(0.5)
				language = input(f"{CREATESHELL}Language: ").strip().title()
				if not language:
					tm.sleep(0.5)
					clear()
					print("Error: Please, empty is not a language. Write a valid language!")
				elif language in ['C', 'Python']:
					tm.sleep(0.5)
					break
				else:
					tm.sleep(0.5)
					clear()
					print(f"Error: '{language}' is not a valid language. Please choose 'C' or 'Python'.")
			while True:
				print("Great, now choose the level you want to start with (It is highly suggested you start with level 0, even if you're already advanced!)\n[0 for beginner and 10 for advanced]")
				tm.sleep(0.5)
				level_entry = input(f"{CREATESHELL}Level: ").strip()
				if not level_entry:
					tm.sleep(0.5)
					clear()
					print("Error: Empty is not a level. Please choose a level!")
				elif level_entry.isdigit():
					level = int(level_entry)
					if 0 <= level <= 10:
						break
					else:
						tm.sleep(0.5)
						clear()
						print("Error: Please enter a level between 0 and 10.")
				else:
					tm.sleep(0.5)
					clear()
					print(f"Error: '{level_entry}' is not a valid integer. Please try again!")
			add_user(login, language, level)
			tm.sleep(0.5)
			print(f"User {login} created as a {language} coder at level {level}!")
			break
	if level > 0:
		while True:
			tm.sleep(0.5)
			print(f"You are currently at level {level}. Do you want to take this simulation at this level or a lower level?\n[You can choose any level between 0 and {level}]")
			tm.sleep(0.5)
			choice = input(f"{CODESHELL}Level: ").strip()
			if not choice:
				tm.sleep(0.5)
				print("Error: Empty is not a level. Please try again!")
				continue
			if not choice.isdigit():
				tm.sleep(0.5)
				print(f"Error: '{choice}' is not an integer. Please try again!")
				continue
			selected_level = int(choice)
			if selected_level > level:
				tm.sleep(0.5)
				print(f"Error: You cannot choose a level higher than {level}.Please choose a level between 0 and {level}.")
			elif 0 <= selected_level <= level:
				break
			else:
				tm.sleep(0.5)
				print(f"Error: Please choose a level between 0 and {level}.")
	else:
		selected_level = 0
	clear()
	tm.sleep(2)
	init_sim = input(f"""You are about to take an exam for {language} programming at level {selected_level}!
You will have 4h:00m:00s to finish this exam and need 100/100 to pass to the level {level + 1}
If you are ready, press ENTER to start!""")
	while init_sim != '':
		init_sim = input("Press ENTER to start!")
	start_countdown(14400)
	finish_stats = 0
	tm.sleep(1)
	while finish_stats != 1 and get_remaining_time() > 0:
		general_score = 0
		try_num = 0
		eval_score = 0
		# assigment = selected_assigment(level)
		assigment_name = "upcoming" #get_assigment_name(level, assigment)
		UPDATETEXT = f"""You are on assigment {assigment_name} for 10 points of your score
You tried this assigment {try_num} times in this session!
Your current score is {eval_score}/100 and still have {format_time(get_remaining_time())} to finish this exam session"""
		print(UPDATETEXT)
		while general_score != 100:
			entry = input(f"{CODESHELL}").strip()
			if entry == "time":
				print(f"You still have {format_time(get_remaining_time())} to finish the test!")
			elif entry == "finish":
				finish_stats = 1
				break
			elif entry == "eval":
				eval_score = 0#eval()
				if eval_score == 100:
					general_score = 100
				else:
					print("FAIL!!!")
					eval_fail = input(f"You still have {format_time(get_remaining_time())} to finish the test.\nPress ENTER to continue!")
					while eval_fail != '':
						print("Press ENTER to continue!")
					eval_fail = None
				pass #implementar a logica de avaliação
			elif entry == "update":
				print(UPDATETEXT)
			else:
				print(f"Error: '{entry}' is not a valid command!")
		continue
	clear()
	letterby('[SIMULATOR ENDED]')
	tm.sleep(2)
	clear()
	for c in range(10, -1, -1):
		print(f"Program will be finished in {c} seconds")
		tm.sleep(1)
		clear()


