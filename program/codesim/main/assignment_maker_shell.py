import sqlite3
import os
from codesim.ft_pylib.cryptographer import encrypt, decrypt
from codesim.utils.colors import *
from codesim.utils.utils_fun import clear
from .simshell import block_signals

ASSIGNMENT_DB_PATH = os.path.expanduser("~/.codesim/program/databases/assignments.db")
MAKER_SHELL = f"{CYAN}Assignment Maker Shell{DEFAULT}: "
HELP = """Create: Create a new assignment.
Clear: Clear the screen.
Exit: Exit the assignment maker shell."""


def init_assigment_db(): # Need to add level_in_level for assigments and assigment_score
    """Initialize the database and create the assigments table if it doesn't exist."""
    conn = sqlite3.connect(ASSIGNMENT_DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS assignments_level
                (language_level TEXT PRIMARY KEY, amount_assigment INTEGER)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS assignments
                (id INTEGER PRIMARY KEY, assignment_languages TEXT, assignment_level INTEGER, assigment_id INTEGER, assignment_name TEXT, assignment_text TEXT, assignment_test TEXT, assignment_output TEXT)''')
    conn.commit()
    conn.close()


def add_assignment(language: str, level: int, assigment_id: int, assignment_name: str, assignment_text: str, assignment_test: str, assignment_output: str):
    """Add a new user to the database."""
    conn = sqlite3.connect(ASSIGNMENT_DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO assignments (assignment_languages, assignment_level, assigment_id, assignment_name, assignment_text, assignment_test, assignment_output) VALUES (?, ?, ?, ?, ?, ?, ?)", (language, level, assigment_id, assignment_name, assignment_text, assignment_test, assignment_output))
    conn.commit()
    conn.close()


def _get_assignment_amount(language: str, level: int) -> int:
    """Get the amount of assigments for a specific language and level."""
    language_level = f"{language}_{level}"
    conn = sqlite3.connect(ASSIGNMENT_DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT amount_assigment FROM assignments_level WHERE language_level = ?", (language_level,))
    amount = cursor.fetchone()
    conn.close()
    return amount[0] if amount else 0


def update_assignment_amount(language: str, level: int, amount: int):
    """Update the amount of assigments for a specific language and level."""
    old_amount = int(_get_assignment_amount(language, level))
    if not old_amount:
        old_amount = 0
    new_amount = old_amount + 1
    language_level = f"{language}_{level}"
    conn = sqlite3.connect(ASSIGNMENT_DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO assignments_level (language_level, amount_assigment) VALUES (?, ?)", (language_level, new_amount))
    conn.commit()
    conn.close()


long_line = "============================================================================="


def register_assignment():
    langs_suffix = {"python": "py", "c": "c", "cpp": "cpp", "java": "java"}
    language = input("Programming language: ").lower()
    level = int(input("Difficulty level (0-10): "))
    assignment_name = input("Name: ")
    allowed_functions = input("Allowed functions (comma separated, leave empty for no restrictions): ")

    print("Assignment Subject(enter'EOF' when finished'):")
    assignment_text = ""
    while True:
        line = input()
        if line.strip() == "EOF":
            break
        assignment_text += line + "\n"
    subject = f"assignment name: {assignment_name}\nfolder to turn in: {assignment_name}/\nfiles to turn in: {assignment_name}.{langs_suffix[language]}\nAllowed functions: {allowed_functions}\n{long_line}\n\n{assignment_text}\n\n{long_line}"

    print("Test code for the assignment (enter'EOF' when finished):")
    assignment_test = ""
    while True:
        line = input()
        if line.strip() == "EOF":
            break
        assignment_test += line + "\n"

    print("Expected output for the assignment (enter 'EOF' when finished):")
    assignment_output = ""
    while True:
        line = input()
        if line.strip() == "EOF":
            break
        assignment_output += line + "\n"
    
    assigment_id = _get_assignment_amount(language, level) + 1
    add_assignment(language=language, level=level, assigment_id=assigment_id, assignment_name=assignment_name, assignment_text=subject, assignment_test=assignment_test, assignment_output=assignment_output)
    update_assignment_amount(language, level, assigment_id)
    print(GREEN + "Assignment added successfully!" + DEFAULT)


def assignment_maker_shell():
    print(GREEN + """#=============================================================================#
#                                                                             #
#                       Welcome to the Assignment Maker!                      #
#                                                                             #
#=============================================================================#
""" + DEFAULT)
    print("type 'help' to see the available options.\n")
    exit_stt = 0;
    while exit_stt != 1:
        with block_signals():
            entry = input(MAKER_SHELL).strip().lower()
            if entry == "help":
                print(f"{YLOW}{HELP}{DEFAULT}")
            elif entry == "clear":
                clear()
            elif entry == "create":
                register_assignment()
            elif entry == "exit":
                exit_stt = 1
            else:
                print(f"{RED}Invalid command. Type 'help' to see the available options.{DEFAULT}")