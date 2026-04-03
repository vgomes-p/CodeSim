import os
import shutil
import sqlite3
from random import shuffle
import importlib

ASSIGNMENT_DB_PATH = os.path.expanduser("~/.codesim/program/databases/assignments.db")

CODESIMDIRS = os.path.expanduser("~/CodeSimDirs/")
SUBJECTS = os.path.expanduser("~/CodeSimDirs/Subject/")
CODEGIT = os.path.expanduser("~/CodeSimDirs/CodeGit/")
TRACEBACK = os.path.expanduser("~/CodeSimDirs/TraceBack/")

def init_mkdirs():
    os.mkdir(CODESIMDIRS)
    os.mkdir(SUBJECTS)
    os.mkdir(CODEGIT)
    os.mkdir(TRACEBACK)


def end_rmdirs():
    shutil.rmtree(SUBJECTS, ignore_errors=True)
    shutil.rmtree(CODEGIT, ignore_errors=True)
    shutil.rmtree(TRACEBACK, ignore_errors=True)
    shutil.rmtree(CODESIMDIRS, ignore_errors=True)


def mk_subject(subject_name: str, subject_text: str):
    dir_path = os.path.expanduser(f"~/CodeSimDirs/Subject/{subject_name}/")
    os.mkdir(dir_path)
    with open(f"{dir_path}/{subject_name}.txt", "w") as f:
        f.write(subject_text)


def get_assignment(language: str, level: int, in_level: int, to_score: int=10):
    language_level = f"{language}_{level}_{in_level}"
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

    cursor.execute("SELECT assignment_name, assignment_score FROM assignments WHERE assignment_languages = ? AND assignment_level = ? AND assignment_in_level = ? AND assigment_id = ?", (language, level, in_level, chosen_assigment))
    result = cursor.fetchone()
    if result is None or result[0] is None:
        raise ValueError(f"No assignment name found for language={language}, level={level}, in_level={in_level}, id={chosen_assigment}")
    subject_name = result[0]
    score = result[1]

    cursor.execute("SELECT assignment_text FROM assignments WHERE assignment_languages = ? AND assignment_level = ? AND assigment_id = ?", (language, level, chosen_assigment))
    result = cursor.fetchone()
    if result is None or result[0] is None:
        raise ValueError(f"No assignment text found for language={language}, level={level}, id={chosen_assigment}")
    subject_text = result[0]

    conn.close()
    mk_subject(subject_name, subject_text)
    to_score -= int(score)
    return subject_name, score, to_score, chosen_assigment
