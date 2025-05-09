from . import simshell
from codesim.utils.database import init_db, remove_user, reset_database
from codesim.utils.utils_fun import clear, letterby
import pkg_resources
import time as tm
import argparse
import sys


def main():
	init_db()

	parser = argparse.ArgumentParser(description="Code Exam Simulator")
	parser.add_argument("--reset-all", action="store_true", help="Delete all takers registered")
	parser.add_argument("--remove-login", help="Remove a specific taker from database")
	parser.add_argument("--version", action="store_true", help="Display the program's version")
	parser.add_argument("--check-update", action="store_true", help="Check if there are any updates available")
	parser.add_argument("--pull", action="store_true", help="Pull the latest update from GitHub")
	parser.add_argument("--install", action="store_true", help="Install the latest updates")
	parser.add_argument("--start", action="store_true", help="Start the simulator")

	args = parser.parse_args()

	if args.version:
		version = pkg_resources.get_distribution("codesim").version
		print(f"codesim version: {version}")
		sys.exit(0)
	elif args.check_update:
		check_for_update()
		sys.exit(0)
	elif args.pull:
		pull_update()
		sys.exit(0)
	elif args.install:
		install_update()
		sys.exit(0)
	elif args.reset_all:
		letterby("Resetting database...")
		reset_database()
		tm.sleep(3)
		letterby("Database reset successfully!")
		sys.exit(0)
	elif args.remove_login:
		letterby(f"Removing user {args.remove_login}...")
		if remove_user(args.remove_login):
			tm.sleep(2)
			letterby(f"User {args.remove_login} removed successfully!")
		else:
			letterby(f"User {args.remove_login} not found.")
		sys.exit(0)
	else:
		tm.sleep(1)
		print("Consider checking for updates with 'codesim --check-update'")
		simshell()


def check_for_update():
	letterby("Checking for updates...")


def pull_update():
	letterby("Pulling updates...")


def install_update():
	letterby("Installing updates...")



if __name__ == "__main__":
	main()