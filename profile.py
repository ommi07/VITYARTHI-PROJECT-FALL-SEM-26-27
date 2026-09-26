def get_non_empty_text(message):
    """Get text that is not empty."""
    while True:
        value = input(message).strip()

        if value:
            return value

        print("This field cannot be empty.")


def create_profile(data):
    """Create a new student profile."""
    print("\n--- CREATE PROFILE ---")

    data["profile"] = {
        "name": get_non_empty_text("Enter your name: "),
        "semester": get_non_empty_text("Enter your semester: "),
        "branch": get_non_empty_text("Enter your branch: "),
        "academic_goal": get_non_empty_text("Enter your main academic goal: ")
    }

    print("\nProfile created successfully.")


def view_profile(data):
    """Display the current profile."""
    profile = data.get("profile", {})

    print("\n--- STUDENT PROFILE ---")

    if not profile:
        print("No profile found.")
        return

    print(f"Name           : {profile.get('name', '-')}")
    print(f"Semester       : {profile.get('semester', '-')}")
    print(f"Branch         : {profile.get('branch', '-')}")
    print(f"Main Goal      : {profile.get('academic_goal', '-')}")


def update_profile(data):
    """Update profile information one field at a time."""
    profile = data.get("profile", {})

    if not profile:
        print("\nNo profile found. Create a profile first.")
        return

    print("\n--- UPDATE PROFILE ---")
    print("Press Enter to keep the current value.")

    name = input(f"Name [{profile.get('name', '')}]: ").strip()
    semester = input(f"Semester [{profile.get('semester', '')}]: ").strip()
    branch = input(f"Branch [{profile.get('branch', '')}]: ").strip()
    goal = input(
        f"Main academic goal [{profile.get('academic_goal', '')}]: "
    ).strip()

    if name:
        profile["name"] = name
    if semester:
        profile["semester"] = semester
    if branch:
        profile["branch"] = branch
    if goal:
        profile["academic_goal"] = goal

    print("\nProfile updated successfully.")


def profile_menu(data):
    """Show the profile submenu."""
    while True:
        print("\n--- STUDENT PROFILE MENU ---")
        print("1. Create / Replace Profile")
        print("2. View Profile")
        print("3. Update Profile")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_profile(data)

        elif choice == "2":
            view_profile(data)

        elif choice == "3":
            update_profile(data)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")
