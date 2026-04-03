import time as tm
import sqlite3
import importlib
import os

ASSIGNMENT_DB_PATH = os.path.expanduser("~/.codesim/program/databases/assignments.db")

def test(entry: str, language: str, score: int=0) -> int:
    return 0

''' assignments
    (
    assignment_languages TEXT,
    assignment_level INTEGER,
    assignment_in_level INTEGER,
    assigment_id INTEGER,
    assignment_score INTEGER,
    assignment_name TEXT,
    assignment_text TEXT,
    assignment_test TEXT,
    assignment_output TEXT
    )'''


def eval(language: str, level: int, in_level: int, assigment_name: str, assigment_id: int) -> int:
    #assignment_path = os.path.expanduser(f"~/CodeSimDirs/Subject/{assigment_name}/{assigment_name}.py")
    #module = importlib.import_module(assignment_path)
    #function = getattr(module, assigment_name)

    #conn = sqlite3.connect(ASSIGNMENT_DB_PATH)
    #cursor = conn.cursor()
    #cursor.execute("SELECT assignment_test FROM assignments WHERE language = ? AND assignment_level = ? AND assignment_in_level = ? AND assignment_id = ?", (language, level, in_level, assigment_id))
    #entry = cursor.fetchone()[0]
    #cursor.execute("SELECT assignment_output FROM assignments WHERE id = ?", (assigment_id,))
    #expected = cursor.fetchone()[0]
    #conn.close()

    #return test(entry=entry, expected=expected, function=function)
    return (100)