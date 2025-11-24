from .simshell import run_program
from codesim.utils.database import init_db, remove_user, reset_database
from codesim.utils.utils_fun import clear, letterby
from packaging import version
import pkg_resources
import time as tm
import subprocess
import requests
import argparse
import sys
import os

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
        clear()
        tm.sleep(1)
        print("Consider checking for updates with 'codesim --check-update'")
        run_program()

def check_for_update():
    letterby("Checking for updates...")
    tm.sleep(1)
    try:
        response = requests.get("https://api.github.com/repos/vgomes-p/CodeSim/releases/latest")
        response.raise_for_status()
        latest_version = response.json()["tag_name"].lstrip("v")
        current_version = pkg_resources.get_distribution("codesim").version
        try:
            latest_ver = version.parse(latest_version)
            current_ver = version.parse(current_version)
            if latest_ver > current_ver:
                letterby(f"Available update: {latest_version}")
                letterby(f"(current: {current_version})")
                letterby("Run 'codesim --pull' to pull it.")
            else:
                letterby("You are using the latest version.")
        except version.InvalidVersion:
            if latest_version != current_version:
                letterby(f"Available update: {latest_version}")
                letterby(f"(current: {current_version})")
                letterby("Run 'codesim --pull' to pull it.")
            else:
                letterby("You are using the latest version.")
    except requests.HTTPError as e:
        print()
        tm.sleep(2)
        if e.response.status_code == 404:
            print("No releases found in the repository. Please wait until a release is created.")
        else:
            print(f"Error checking for update: {e}")
    except requests.RequestException as e:
        print()
        tm.sleep(2)
        print(f"Network error checking for update: {e}")
    except Exception as e:
        print()
        tm.sleep(2)
        print(f"Unexpected error: {e}")

repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def pull_update():
    letterby("Pulling updates...")
    tm.sleep(1)
    try:
        subprocess.run(["git", "pull", "origin", "main"], cwd=repo_root, check=True, text=True, capture_output=True)
        letterby("Updates pulled successfully.")
        letterby("Run 'codesim --install' to install it.")
    except subprocess.CalledProcessError as e:
        print()
        tm.sleep(2)
        print(f"Error pulling updates: {e.stderr if e.stderr else e}")
        if "There is no tracking information" in e.stderr:
            print("Try setting up tracking with: git branch --set-upstream-to=origin/main main")
    except FileNotFoundError:
        print()
        tm.sleep(2)
        print("Error: Git is not installed or not found in PATH.")
    except OSError as e:
        print()
        tm.sleep(2)
        print(f"Error accessing repository directory: {e}")

def install_update():
    letterby("Installing updates...")
    tm.sleep(1)
    try:
        subprocess.run(["sudo", "pip", "install", "-e", "."], cwd=repo_root, check=True, text=True, capture_output=True)
        letterby("Updates installed successfully.")
    except subprocess.CalledProcessError as e:
        print()
        tm.sleep(2)
        print(f"Error installing updates: {e.stderr if e.stderr else e}")
    except FileNotFoundError:
        print()
        tm.sleep(2)
        print("Error: pip is not installed or not found in PATH.")
    except OSError as e:
        print()
        tm.sleep(2)
        print(f"Error accessing repository directory: {e}")

if __name__ == "__main__":
    main()