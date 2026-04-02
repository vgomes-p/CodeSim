import time as tm
import sqlite3
import importlib
import os

ASSIGNMENT_DB_PATH = os.path.expanduser("~/.codesim/databases/assignments.db")

def test(entry: str, language: str, score: int=0) -> int:
    return 0


def eval(assigment_name: str, assigment_folder: str, assigment_id: int) -> int:
    module = importlib.import_module(assigment_folder)
    function = getattr(module, assigment_name)

    conn = sqlite3.connect(ASSIGNMENT_DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT entry FROM assignments WHERE id = ?", (assigment_id,))
    entry = cursor.fetchone()[0]
    cursor.execute("SELECT expected FROM assignments WHERE id = ?", (assigment_id,))
    expected = cursor.fetchone()[0]
    conn.close()

    return test(entry=entry, expected=expected, function=function)