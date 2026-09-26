from activities import ACTIVITY_CATEGORIES, find_record_by_date


def get_number(prompt):
    """Get a valid number/value from the user."""
    while True:
        try:
            value = float(input(prompt))

            if value < 0:
                print("The value cannot be negative.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def print_analysis(record):
    """Print a rule-based analysis of one daily record."""
    study = float(record.get("study", 0))
    classes = float(record.get("classes", 0))
    sleep = float(record.get("sleep", 0))
    exercise = float(record.get("exercise", 0))
    entertainment = float(record.get("entertainment", 0))
    social = float(record.get("social", 0))
    travel = float(record.get("travel", 0))
    other = float(record.get("other", 0))

    academic_time = study + classes
    total = study + classes + sleep + exercise + entertainment
    total += social + travel + other
    free_time = max(0, 24 - total)

    print("\n" + "=" * 55)
    print("              DAILY ROUTINE ANALYSIS")
    print("=" * 55)

    print(f"\nStudy hours          : {study:.2f}")
    print(f"Class hours          : {classes:.2f}")
    print(f"Academic time        : {academic_time:.2f}")
    print(f"Sleep hours          : {sleep:.2f}")
    print(f"Exercise hours       : {exercise:.2f}")
    print(f"Entertainment hours  : {entertainment:.2f}")
    print(f"Free/unallocated time: {free_time:.2f}")

    print("\nTIME BALANCE")
    print("-" * 55)

    if academic_time > 0:
        academic_percent = (academic_time / 24) * 100
    else:
        academic_percent = 0

    sleep_percent = (sleep / 24) * 100
    entertainment_percent = (entertainment / 24) * 100

    print(f"Academic time        : {academic_percent:.1f}% of the day")
    print(f"Sleep                : {sleep_percent:.1f}% of the day")
    print(f"Entertainment        : {entertainment_percent:.1f}% of the day")

    print("\nRULE-BASED OBSERVATIONS")
    print("-" * 55)

    observations = []

    if study >= 3:
        observations.append("Study time reached 3 hours or more.")
    else:
        observations.append("Study time is below 3 hours.")

    if 6 <= sleep <= 9:
        observations.append("Sleep time is within the selected 6-9 hour range.")
    elif sleep < 6:
        observations.append("Sleep time is below 6 hours.")
    else:
        observations.append("Sleep time is above 9 hours.")

    if exercise > 0:
        observations.append("Exercise was included in the routine.")
    else:
        observations.append("No exercise was recorded.")

    if entertainment > study:
        observations.append("Entertainment time is higher than study time.")
    else:
        observations.append("Study time is at least as high as entertainment time.")

    if academic_time >= 6:
        observations.append("Academic time reached 6 hours or more.")
    else:
        observations.append("Academic time is below 6 hours.")

    for number, observation in enumerate(observations, start=1):
        print(f"{number}. {observation}")

    print("\nNote: This is a simple rule-based analysis, not a scientific")
    print("measurement of productivity.")


def analyze_day(data):
    """Analyze a selected daily record."""
    if not data["activities"]:
        print("\nNo activity records found.")
        return

    print("\n--- ANALYZE MY DAY ---")
    date = input("Enter date (YYYY-MM-DD): ").strip()

    record = find_record_by_date(data, date)

    if record is None:
        print("No record found for that date.")
        return

    print_analysis(record)
