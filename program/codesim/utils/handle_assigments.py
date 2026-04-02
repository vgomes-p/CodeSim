import os
import sqlite3
from random import shuffle
import importlib

ASSIGNMENT_DB_PATH = os.path.expanduser("~/.codesim/databases/assignments.db")

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
    #language_level = f"{language}_{level}"
    #conn = sqlite3.connect(ASSIGNMENT_DB_PATH)
    #cursor = conn.cursor()
    #cursor.execute("SELECT amount_assigment FROM assigment_levels WHERE language_level = ?", (language_level,))
    #how_many_assigments = cursor.fetchone()[0]
    #arr_assigment = [int(i) for i in range(1, how_many_assigments)]
    #shuffle(arr_assigment)
    #chosen_assigment = arr_assigment[0]
    #cursor.execute("SELECT assignment_name FROM assignments WHERE assignment_languages = ? AND assignment_level = ? AND assigment_id = ?", (language, level, chosen_assigment))
    #subject_name = cursor.fetchone()[0]
    #cursor.execute("SELECT assignment_text FROM assignments WHERE assignment_languages = ? AND assignment_level = ? AND assigment_id = ?", (language, level, chosen_assigment))
    #subject_text = cursor.fetchone()[0]
    #conn.close()
    subject_text = "This is an upcoming assignment. Stay tuned!"
    subject_name = "upcoming"
    mk_subject(subject_name, subject_text)
    return subject_name
