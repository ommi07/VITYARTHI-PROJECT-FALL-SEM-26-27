def get_positive_number(prompt):
    """Get a positive number."""
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("Enter a number greater than 0.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def get_progress(prompt):
    """Get progress between 0 and 100."""
    while True:
        try:
            value = float(input(prompt))

            if value < 0 or value > 100:
                print("Progress must be between 0 and 100.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def get_goal_id(data):
    """Get the next unused goal ID."""
    goal_id = 1

    for goal in data["goals"]:
        current_id = goal.get("id", 0)

        if isinstance(current_id, int) and current_id >= goal_id:
            goal_id = current_id + 1

    return goal_id


def find_goal(data, goal_id):
    """Find a goal by its ID."""
    for goal in data["goals"]:
        if goal.get("id") == goal_id:
            return goal

    return None


def add_goal(data):
    """Add a new academic goal."""
    print("\n--- ADD ACADEMIC GOAL ---")

    title = input("Enter goal title: ").strip()

    if not title:
        print("Goal title cannot be empty.")
        return

    deadline = input("Enter deadline (optional): ").strip()
    target = get_positive_number("Enter target value: ")
    unit = input("Enter target unit (hours, questions, chapters, etc.): ").strip()

    if not unit:
        unit = "units"

    goal = {
        "id": get_goal_id(data),
        "title": title,
        "deadline": deadline,
        "target": target,
        "unit": unit,
        "progress": 0
    }

    data["goals"].append(goal)

    print("\nGoal added successfully.")


def view_goals(data):
    """Display all academic goals."""
    print("\n--- ACADEMIC GOALS ---")

    if not data["goals"]:
        print("No goals found.")
        return

    for goal in data["goals"]:
        progress = float(goal.get("progress", 0))
        status = "Completed" if progress >= 100 else "In Progress"

        print("\n" + "-" * 50)
        print(f"ID        : {goal.get('id', '-')}")
        print(f"Goal      : {goal.get('title', '-')}")
        print(f"Deadline  : {goal.get('deadline', '-') or 'Not set'}")
        print(f"Target    : {goal.get('target', 0)} {goal.get('unit', '')}")
        print(f"Progress  : {progress:.1f}%")
        print(f"Status    : {status}")


def update_goal(data):
    """Update goal progress and details."""
    print("\n--- UPDATE GOAL ---")

    if not data["goals"]:
        print("No goals found.")
        return

    view_goals(data)

    try:
        goal_id = int(input("\nEnter goal ID: "))
    except ValueError:
        print("Please enter a valid goal ID.")
        return

    goal = find_goal(data, goal_id)

    if goal is None:
        print("Goal not found.")
        return

    print("\nPress Enter to keep the current value.")

    title = input(f"Title [{goal.get('title', '')}]: ").strip()
    deadline = input(
        f"Deadline [{goal.get('deadline', '')}]: "
    ).strip()

    current_progress = float(goal.get("progress", 0))
    progress_text = input(
        f"Progress [{current_progress}%]: "
    ).strip()

    if title:
        goal["title"] = title

    if deadline:
        goal["deadline"] = deadline

    if progress_text:
        try:
            progress = float(progress_text)

            if progress < 0 or progress > 100:
                print("Progress must be between 0 and 100. Update cancelled.")
                return

            goal["progress"] = progress

        except ValueError:
            print("Invalid progress. Update cancelled.")
            return

    print("\nGoal updated successfully.")


def goal_menu(data):
    """Show the academic goals submenu."""
    while True:
        print("\n--- ACADEMIC GOALS MENU ---")
        print("1. Add Goal")
        print("2. View Goals")
        print("3. Update Goal")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_goal(data)

        elif choice == "2":
            view_goals(data)

        elif choice == "3":
            update_goal(data)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")
