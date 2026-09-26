from activities import ACTIVITY_CATEGORIES, find_record_by_date


def get_change():
    """Get a valid routine change."""
    while True:
        try:
            value = float(input("Enter change in hours (+ increase / - decrease): "))

            return value

        except ValueError:
            print("Please enter a valid number.")


def simulate_routine(data):
    """Create a simple what-if routine simulation."""
    print("\n" + "=" * 55)
    print("                ROUTINE SIMULATOR")
    print("=" * 55)

    if not data["activities"]:
        print("\nNo activity records found.")
        print("Add a daily record before using the simulator.")
        return

    date = input("\nEnter the date to simulate (YYYY-MM-DD): ").strip()
    record = find_record_by_date(data, date)

    if record is None:
        print("No record found for that date.")
        return

    simulated = {}

    for category in ACTIVITY_CATEGORIES:
        simulated[category] = float(record.get(category, 0))

    print("\nCurrent routine:")
    print("-" * 40)

    for category in ACTIVITY_CATEGORIES:
        print(f"{category.title():15}: {simulated[category]:.2f} hrs")

    print("\nChoose one activity to change.")

    for number, category in enumerate(ACTIVITY_CATEGORIES, start=1):
        print(f"{number}. {category.title()}")

    try:
        choice = int(input("Enter activity number: "))
    except ValueError:
        print("Invalid choice.")
        return

    if choice < 1 or choice > len(ACTIVITY_CATEGORIES):
        print("Invalid activity number.")
        return

    category = ACTIVITY_CATEGORIES[choice - 1]
    change = get_change()

    new_value = simulated[category] + change

    if new_value < 0:
        print("\nThe simulated value cannot be negative.")
        return

    simulated[category] = new_value

    current_total = sum(float(record.get(item, 0)) for item in ACTIVITY_CATEGORIES)
    simulated_total = sum(simulated.values())

    print("\nCURRENT ROUTINE")
    print("-" * 40)

    for item in ACTIVITY_CATEGORIES:
        print(f"{item.title():15}: {float(record.get(item, 0)):.2f} hrs")

    print(f"{'Total':15}: {current_total:.2f} hrs")

    print("\nSIMULATED ROUTINE")
    print("-" * 40)

    for item in ACTIVITY_CATEGORIES:
        difference = simulated[item] - float(record.get(item, 0))
        sign = "+" if difference > 0 else ""

        print(
            f"{item.title():15}: {simulated[item]:.2f} hrs "
            f"({sign}{difference:.2f})"
        )

    print(f"{'Total':15}: {simulated_total:.2f} hrs")

    if simulated_total > 24:
        excess = simulated_total - 24

        print(
            f"\nWARNING: Simulated routine exceeds 24 hours by "
            f"{excess:.2f} hour(s)."
        )
        print(
            f"You need to reduce at least {excess:.2f} hour(s) "
            "from other activities."
        )

    elif simulated_total < 24:
        remaining = 24 - simulated_total

        print(
            f"\nThe simulated routine has {remaining:.2f} "
            "unallocated hour(s)."
        )

    else:
        print("\nThe simulated routine uses exactly 24 hours.")

    print("\nSimulation complete. The original record was not changed.")
