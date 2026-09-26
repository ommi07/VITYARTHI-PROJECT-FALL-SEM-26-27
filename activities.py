from datetime import datetime


ACTIVITY_CATEGORIES = (
    "study",
    "classes",
    "sleep",
    "exercise",
    "entertainment",
    "social",
    "other"
)


def get_valid_date():
    """Get a valid date in YYYY-MM-DD format."""
    while True:
        date_text = input("Enter date (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            return date_text
        except ValueError:
            print("Invalid date. Use the format YYYY-MM-DD.")


def get_hours(activity_name):
    """Get a non-negative number of hours."""
    while True:
        try:
            hours = float(input(f"Enter {activity_name} hours: "))

            if hours < 0:
                print("Hours cannot be negative.")
                continue

            return hours

        except ValueError:
            print("Please enter a valid number.")


def find_record_by_date(data, date):
    """Find the activity record for a date."""
    for record in data["activities"]:
        if record.get("date") == date:
            return record

    return None


def calculate_total(record):
    """Calculate the total hours in one record."""
    total = 0

    for category in ACTIVITY_CATEGORIES:
        total += float(record.get(category, 0))

    return total


def enter_activity_values():
    """Enter all activity hours."""
    record = {}

    for category in ACTIVITY_CATEGORIES:
        record[category] = get_hours(category)

    total = calculate_total(record)

    if total > 24:
        print(f"\nTotal time is {total:.2f} hours.")
        print("A day cannot contain more than 24 hours.")
        return None

    record["total_hours"] = round(total, 2)
    return record


def add_record(data):
    """Add one daily activity record."""
    print("\n--- ADD DAILY RECORD ---")

    date = get_valid_date()

    if find_record_by_date(data, date) is not None:
        print("\nA record already exists for this date.")
        print("Please use Edit Record to change it.")
        return

    record = enter_activity_values()

    if record is None:
        return

    record["date"] = date
    data["activities"].append(record)
    data["activities"].sort(key=lambda item: item.get("date", ""))

    print("\nDaily record added successfully.")


def view_records(data):
    """Display all daily records."""
    print("\n--- DAILY RECORDS ---")

    if not data["activities"]:
        print("No activity records found.")
        return

    for record in data["activities"]:
        print("\nDate:", record.get("date", "-"))

        for category in ACTIVITY_CATEGORIES:
            print(f"{category.title():15}: {float(record.get(category, 0)):.2f} hrs")

        print(f"{'Total':15}: {float(record.get('total_hours', 0)):.2f} hrs")


def edit_record(data):
    """Edit an existing daily record."""
    print("\n--- EDIT DAILY RECORD ---")

    if not data["activities"]:
        print("No activity records found.")
        return

    date = get_valid_date()
    record = find_record_by_date(data, date)

    if record is None:
        print("No record found for that date.")
        return

    print("Enter the new values for this date.")
    new_values = enter_activity_values()

    if new_values is None:
        return

    for category in ACTIVITY_CATEGORIES:
        record[category] = new_values[category]

    record["total_hours"] = new_values["total_hours"]

    print("\nDaily record updated successfully.")


def delete_record(data):
    """Delete a daily activity record."""
    print("\n--- DELETE DAILY RECORD ---")

    if not data["activities"]:
        print("No activity records found.")
        return

    date = get_valid_date()
    record = find_record_by_date(data, date)

    if record is None:
        print("No record found for that date.")
        return

    confirm = input(
        f"Delete the record for {date}? (y/n): "
    ).strip().lower()

    if confirm == "y":
        data["activities"].remove(record)
        print("Record deleted successfully.")
    else:
        print("Deletion cancelled.")


def activity_menu(data):
    """Show the daily activity submenu."""
    while True:
        print("\n--- DAILY ACTIVITY TRACKER MENU ---")
        print("1. Add Record")
        print("2. View Records")
        print("3. Edit Record")
        print("4. Delete Record")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_record(data)

        elif choice == "2":
            view_records(data)

        elif choice == "3":
            edit_record(data)

        elif choice == "4":
            delete_record(data)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")
