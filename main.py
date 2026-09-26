import os
import json

from profile import profile_menu
from activities import activity_menu
from analysis import analyze_day
from goals import goal_menu
from simulator import simulate_routine
from reports import show_history, generate_report

DATA_FOLDER = "data"
DATA_FILE = os.path.join(DATA_FOLDER, "student_data.json")


def load_data():
    """Load data from JSON file."""
    os.makedirs(DATA_FOLDER, exist_ok=True)

    if not os.path.exists(DATA_FILE):
        return {
            "profile": {},
            "activities": [],
            "goals": []
        }

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary.")

        data.setdefault("profile", {})
        data.setdefault("activities", [])
        data.setdefault("goals", [])
        return data

    except (json.JSONDecodeError, OSError, ValueError):
        print("\nCould not read the saved data.")
        print("A new empty data set will be used.")
        return {
            "profile": {},
            "activities": [],
            "goals": []
        }


def save_data(data):
    """Save data to JSON file."""
    os.makedirs(DATA_FOLDER, exist_ok=True)

    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        return True
    except OSError:
        print("\nCould not save the data file.")
        return False


def print_header():
    print("\n" + "=" * 55)
    print("       STUDENT PRODUCTIVITY SIMULATOR")
    print("=" * 55)


def main_menu(data):
    while True:
        print_header()

        name = data["profile"].get("name", "Student")
        print(f"\nWelcome, {name}!")

        print("\nMAIN MENU")
        print("-" * 55)
        print("1. Student Profile")
        print("2. Daily Activity Tracker")
        print("3. Analyze My Day")
        print("4. Academic Goals")
        print("5. Routine Simulator")
        print("6. Progress History")
        print("7. Generate Report")
        print("8. Exit")
        print("-" * 55)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            profile_menu(data)
            save_data(data)

        elif choice == "2":
            activity_menu(data)
            save_data(data)

        elif choice == "3":
            analyze_day(data)

        elif choice == "4":
            goal_menu(data)
            save_data(data)

        elif choice == "5":
            simulate_routine(data)

        elif choice == "6":
            show_history(data)

        elif choice == "7":
            generate_report(data)

        elif choice == "8":
            save_data(data)
            print("\nData saved successfully.")
            print("Thank you for using Student Productivity Simulator.")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 8.")


def main():
    data = load_data()
    main_menu(data)


if __name__ == "__main__":
    main()
