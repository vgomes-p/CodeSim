import os
import sqlite3
from random import shuffle
import importlib

ASSIGNMENT_DB_PATH = os.path.expanduser("~/.codesim/program/databases/assignments.db")

def init_mkdirs():
    os.mkdir("~/CodeSimDirs")
    os.mkdir("~/CodeSimDirs/Subject")
    os.mkdir("~/CodeSimDirs/CodeGit")
    os.mkdir("~/CodeSimDirs/TraceBack")


def end_rmdirs():
    os.rmdir("~/CodeSimDirs/Subject")
    os.rmdir("~/CodeSimDirs/CodeGit")
    os.rmdir("~/CodeSimDirs/TraceBack")
    os.rmdir("~/CodeSimDirs")


def mk_subject(subject_name: str, subject_text: str):
    os.mkdir(f"~/CodeSimDirs/Subject/{subject_name}")
    with open(f"~/CodeSimDirs/Subject/{subject_name}/{subject_name}.txt", "w") as f:
        f.write(subject_text)


def get_assignment(language: str, level: int, in_level: int) -> str:
    language_level = f"{language}_{level}"
    conn = sqlite3.connect(ASSIGNMENT_DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT amount_assigment FROM assignments_level WHERE language_level = ?", (language_level,))
    result = cursor.fetchone()
    if result is None or result[0] is None:
        raise ValueError(f"No assignment count found for language_level: {language_level}")
    how_many_assigments = int(result[0])
    if how_many_assigments < 1:
        raise ValueError(f"Invalid assignment count for language_level {language_level}: {how_many_assigments}")
    arr_assigment = list(range(1, how_many_assigments + 1))
    shuffle(arr_assigment)
    chosen_assigment = arr_assigment[0]

    cursor.execute("SELECT assignment_name FROM assignments WHERE assignment_languages = ? AND assignment_level = ? AND assigment_id = ?", (language, level, chosen_assigment))
    result = cursor.fetchone()
    if result is None or result[0] is None:
        raise ValueError(f"No assignment name found for language={language}, level={level}, id={chosen_assigment}")
    subject_name = result[0]

    cursor.execute("SELECT assignment_text FROM assignments WHERE assignment_languages = ? AND assignment_level = ? AND assigment_id = ?", (language, level, chosen_assigment))
    result = cursor.fetchone()
    if result is None or result[0] is None:
        raise ValueError(f"No assignment text found for language={language}, level={level}, id={chosen_assigment}")
    subject_text = result[0]

    conn.close()
    mk_subject(subject_name, subject_text)
    return subject_name
