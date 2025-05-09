import sqlite3
import os

DB_PATH = os.path.expanduser("~/codesim.db")

def init_db():
	"""Initialize the database and create the users table if it doesn't exist."""
	conn = sqlite3.connect(DB_PATH)
	c = conn.cursor()
	c.execute('''CREATE TABLE IF NOT EXISTS users
				 (login TEXT PRIMARY KEY, language TEXT, level INTEGER)''')
	conn.commit()
	conn.close()

def add_user(login, language, level):
	"""Add a new user to the database."""
	conn = sqlite3.connect(DB_PATH)
	c = conn.cursor()
	c.execute("INSERT INTO users (login, language, level) VALUES (?, ?, ?)", (login, language, level))
	conn.commit()
	conn.close()

def get_user(login):
	"""Retrieve a user's data by login. Returns None if not found."""
	conn = sqlite3.connect(DB_PATH)
	c = conn.cursor()
	c.execute("SELECT login, language, level FROM users WHERE login = ?", (login,))
	user = c.fetchone()
	conn.close()
	if user:
		return {"login": user[0], "language": user[1], "level": user[2]}
	return None

def remove_user(login):
	"""Remove a user from the database. Returns True if successful, False if user not found."""
	conn = sqlite3.connect(DB_PATH)
	c = conn.cursor()
	c.execute("DELETE FROM users WHERE login = ?", (login,))
	affected = c.rowcount
	conn.commit()
	conn.close()
	return affected > 0

def reset_database():
	"""Reset the database by dropping and recreating the users table."""
	conn = sqlite3.connect(DB_PATH)
	c = conn.cursor()
	c.execute("DROP TABLE IF EXISTS users")
	conn.commit()
	conn.close()
	init_db()

def user_exists(login):
	"""Check if a user exists in the database."""
	return get_user(login) is not None