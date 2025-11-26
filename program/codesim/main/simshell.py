#Imports
from codesim.utils.countdown import format_time, start_countdown, get_remaining_time
from codesim.utils.database import add_user, get_user, user_exists
from codesim.utils.utils_fun import clear, letterby, press_enter
from codesim.eval.eval import eval
from contextlib import contextmanager
from codesim.utils.colors import *
import time as tm
import signal


# General Variables
CODESHELL = GREEN + 'codeshell $> ' + DEFAULT
CREATESHELL = CYAN + 'USER CREATOR $> ' + DEFAULT
SIMTEXT = f"""{PINK}<<< COMMANDS AVAILABLE >>>{DEFAULT}
{CYAN}help:{DEFAULT} shows this message
{CYAN}clear:{DEFAULT} clear the terminal
{CYAN}eval:{DEFAULT} evaluate
{CYAN}finish:{DEFAULT} end the exam
{CYAN}time:{DEFAULT} show much time rest
{CYAN}update:{DEFAULT} shows exam current status"""

#languages
valid_languages = ["Python"]


@contextmanager
# Method to prevent user from ending the exam using ctrl
def block_signals():
    o_sigint = signal.getsignal(signal.SIGINT)
    o_sigquit = signal.getsignal(signal.SIGQUIT)
    def do_noth(*args):
        pass
    signal.signal(signal.SIGINT, do_noth)
    signal.signal(signal.SIGQUIT, do_noth)
    try:
        yield
    finally:
        signal.signal(signal.SIGINT, o_sigint)
        signal.signal(signal.SIGQUIT, o_sigquit)

def create_new_user(login: str) -> tuple[str, str]:
    letterby(f"No user found for '{login}'. Creating a new user...")
    tm.sleep(0.5)
    while True:
        print("Which language do you study? (we have simulation for Python only!)")
        tm.sleep(0.5)
        language = input(f"{CREATESHELL}Language: ").strip().title() # Get language
        if not language:
            tm.sleep(0.5)
            clear()
            print(RED, "Error: Please, empty is not a language. Write a valid language!", DEFAULT)
        elif language in valid_languages:
            tm.sleep(0.5)
            break
        else:
            tm.sleep(0.5)
            clear()
            print(RED, f"Error: '{language}' is not a valid language. Please choose one of the following language:\n{str(valid_languages).replace("[", "").replace("]", "").replace('"', "")}.", DEFAULT)
    while True:
        print("Great, now choose the level you want to start with (It is highly suggested you start with level 0, even if you're already advanced!)\n[0 for beginner and 10 for advanced]")
        tm.sleep(0.5)
        level_entry = input(f"{CREATESHELL}Level: ").strip() # Get language knowledge level
        if not level_entry:
            tm.sleep(0.5)
            clear()
            print(RED, "Error: Empty is not a level. Please choose a level!", DEFAULT)
        elif level_entry.isdigit():
            level = int(level_entry)
            if 0 <= level <= 10:
                break
            else:
                tm.sleep(0.5)
                clear()
                print(RED, "Error: Please enter a level between 0 and 10.", DEFAULT)
        else:
            tm.sleep(0.5)
            clear()
            print(RED, f"Error: '{level_entry}' is not a valid integer. Please try again!", DEFAULT)
    add_user(login, language, level) # Send user, language and level to the database
    tm.sleep(0.5)
    print(f"User {CYAN + login + DEFAULT} created as a {CYAN + language + DEFAULT} coder at level {CYAN + str(level) + DEFAULT}!")
    return language, level

def welcome() -> tuple[str, str]:
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
        user = get_user(login) # Check if the login exists in database
        if user:
            print(f"Welcome back, {CYAN + login + DEFAULT}! {CYAN + user['language'] + DEFAULT} coder at level {CYAN + str(user['level']) + DEFAULT}...")
            language = user['language']
            level = user['level']
            return language, level
        else:
            language, level = create_new_user(login=login)
            return language, level

def select_level(actual_level: int) -> str:
    if actual_level > 0: #if user's language knowledge level is not 0, ask which level they want to take the test (ask it everytime while user level for any user whose level is bigger than 0, so the user may choose to take exam from previous level)
        while True:
            tm.sleep(0.5)
            print(f"You are currently at level {CYAN + str(actual_level) + DEFAULT}. Do you want to take this simulation at this level or a lower level?\n[You can choose any level between 0 and {actual_level}]")
            tm.sleep(0.5)
            choice = input(f"{CODESHELL}Level: ").strip()
            if not choice:
                tm.sleep(0.5)
                print(RED, "Error: Empty is not a level. Please try again!", DEFAULT)
                continue
            if not choice.isdigit():
                tm.sleep(0.5)
                print(RED, f"Error: '{choice}' is not an integer. Please try again!", DEFAULT)
                continue
            selected_level = int(choice)
            if selected_level > actual_level: # Do not allow user to take a test from a level higher than their current level
                tm.sleep(0.5)
                print(RED, f"Error: You cannot choose a level higher than {actual_level}. Please choose a level between 0 and {actual_level}.", DEFAULT)
            elif 0 <= selected_level <= actual_level:
                return selected_level
            else:
                tm.sleep(0.5)
                print(RED, f"Error: Please choose a level between 0 and {actual_level}.", DEFAULT)
    else:
        return str(0) #if user level is 0, set selected level as 0, since they cannot choose any other level

def intro_text(language: str, selected_level: str):
    tm.sleep(2)
    print(f"""You are about to take an exam for {YLOW + language + DEFAULT} programming at level {YLOW + str(selected_level) + DEFAULT}!
You need {YLOW}100/100{DEFAULT} to pass to level {PINK + str(selected_level + 1) + DEFAULT}.
You will have {CYAN}4h:00m:00s{DEFAULT} to finish this exam.
If you are ready, press ENTER to start!""")
    press_enter()

def update_text(actual_assigment_name: str, remaining_time: str, try_num: int, general_score: int):
    tm.sleep(2)
    print(f"""{PINK}<<< UPDATE >>>{DEFAULT}
You are working on assignment {CYAN + actual_assigment_name + DEFAULT}, worth 10 points.
You have attempted this assignment {PINK + str(try_num) + DEFAULT} time(s) during this session.
Your current score is {YLOW + str(general_score)}/100{DEFAULT}.
You still have {CYAN + remaining_time + DEFAULT} remaining to finish this exam session.
Press ENTER to continue!""")
    press_enter()

def new_assigment_text(actual_assigment_name: str, remaining_time: str, try_num: int, general_score: int):
    tm.sleep(2)
    print(f"""{PINK}<<< NEW ASSIGNMENT >>>{DEFAULT}
You are not working on assignment {CYAN + actual_assigment_name + DEFAULT}, worth 10 points.
You have attempted this assignment {PINK + str(try_num) + DEFAULT} time(s) during this session.
Your current score is {YLOW + str(general_score)}/100{DEFAULT}.
You still have {CYAN + remaining_time + DEFAULT} remaining to finish this exam session.
Press ENTER to continue!""")
    press_enter()

def _finish(actual_assigment_name: str, remaining_time: str, general_score: int) -> int:
    valid_ret = ['r', 'f']
    print(f"""{RED}<<< ARE YOU SURE YOU WANT TO FINISH THIS SESSION? >>>{DEFAULT}
You are working on assignment {CYAN + actual_assigment_name + DEFAULT}.
You already scored {PINK + str(general_score) + "/100" + DEFAULT}.
You still have {CYAN + remaining_time + DEFAULT} remaining to finish this exam session.
{PINK}['r' or any entry to return to session and 'f' to finish]""")
    ret = input(CODESHELL).lower()
    if not ret:
        clear()
        print("Entry not accepted, returning to session")
        return 0
    if ret not in valid_ret:
        clear()
        print("Entry not accepted, returning to session")
        return 0
    if ret == 'r':
        clear()
        print("Returning to session")
        return 0
    else:
        return 1

def simshell(init_assigment: str, remaining_time: str, selected_level: str, actual_level: str, try_num: int, general_score: int):
    print(SIMTEXT)
    update_text(actual_assigment_name=init_assigment, remaining_time=remaining_time, try_num=try_num, general_score=general_score)
    finish_stats = 0 # create a holder for "finish" command signal
    while finish_stats != 1 and get_remaining_time() > 0: #Main loop that will run while finish signal is not given and time it not out
        assignment_name = init_assigment
        while get_remaining_time() > 0 and general_score != 100:
            with block_signals():
                try:
                    entry = input(CODESHELL).strip().lower()
                    if entry == "time":
                        print(f"You still have {CYAN + format_time(get_remaining_time()) + DEFAULT} remaining to finish this exam session!")
                    elif entry == "finish":
                        fret = _finish(actual_assigment_name=assignment_name, remaining_time=remaining_time, general_score=general_score)
                        if fret == 0:
                            update_text(actual_assigment_name=assignment_name, remaining_time=remaining_time, try_num=try_num, general_score=general_score)
                        else:
                            finish_stats = 1
                            break
                    elif entry == "eval":
                        eval_score = 100 #eval()
                        if eval_score == 100:
                            general_score += 10
                            try_num = 0
                            assignment_name = "new_assignment()"
                            new_assigment_text(actual_assigment_name=assignment_name, remaining_time=remaining_time, try_num=try_num, general_score=general_score)
                        else:
                            try_num += 1
                            print(RED, BOLD, "××× ASSIGNMENT FAILED ×××", DEFAULT, sep='')
                            print(f"You still have {CYAN + format_time(get_remaining_time()) + DEFAULT}  remaining to finish this exam session.\nPress ENTER to continue!")
                            press_enter()
                    elif entry == "update":
                        update_text(actual_assigment_name=assignment_name, remaining_time=remaining_time, try_num=try_num, general_score=general_score)
                    elif entry == "clear":
                        clear()
                    elif entry == "help":
                        print(SIMTEXT)
                    else:
                        print(RED, "Error:", DEFAULT, YLOW, f" '{entry}'", DEFAULT, " is not a valid command! run 'help' to see valid commands!", sep='')
                except EOFError:
                    pass
        if general_score == 100 or finish_stats == 1:
            if selected_level == actual_level:
                #print(f"Congrats on passing to the next level!")
                # CREATE A FUNCTION TO UPDATE THE DATABASE
                return 0
            else:
                return 0
        print("time is up")
        return 0
    return 0

def finish_program():
    clear()
    letterby('[SIMULATOR ENDED]')
    tm.sleep(2)
    clear()
    for c in range(10, -1, -1):
        print(f"Program will be finished in {c} seconds")
        tm.sleep(1)
        clear()

def run_program():
    global general_score, try_num, eval_score # Global vars for score, how many tries, and assigment score
    general_score = 0
    try_num = 0
    eval_score = 0
    language, level = welcome()
    selected_level = select_level(actual_level=level)
    clear()
    intro_text(language=language, selected_level=selected_level)
    start_countdown(14400) #start time countdown
    tm.sleep(1)
    assignment_name = "upcoming"  #wip: função que pega nome do execicio || Get assigment name
    remaining_time = str(format_time(get_remaining_time()))
    simshell(init_assigment=assignment_name, remaining_time=remaining_time, selected_level=selected_level, actual_level=level, try_num=try_num, general_score=general_score)
    finish_program()
    return 0