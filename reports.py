def show_history(data):
    """Display activity history and basic study summaries."""
    print("\n" + "=" * 55)
    print("                 PROGRESS HISTORY")
    print("=" * 55)

    if not data["activities"]:
        print("\nNo activity history found.")
    else:
        total_study = 0
        total_academic = 0

        print("\nDAILY STUDY HISTORY")
        print("-" * 55)
        print(f"{'Date':15} {'Study':10} {'Classes':10} {'Academic':10}")

        for record in data["activities"]:
            study = float(record.get("study", 0))
            classes = float(record.get("classes", 0))
            academic = study + classes

            total_study += study
            total_academic += academic

            print(
                f"{record.get('date', '-'):15} "
                f"{study:<10.2f} "
                f"{classes:<10.2f} "
                f"{academic:<10.2f}"
            )

        print("-" * 55)
        print(f"Total study hours   : {total_study:.2f}")
        print(f"Total academic hours: {total_academic:.2f}")

    print("\nACADEMIC GOAL PROGRESS")
    print("-" * 55)

    if not data["goals"]:
        print("No goals found.")
        return

    for goal in data["goals"]:
        progress = float(goal.get("progress", 0))
        status = "Completed" if progress >= 100 else "In Progress"

        print(
            f"{goal.get('id', '-')}. "
            f"{goal.get('title', '-')} - "
            f"{progress:.1f}% - {status}"
        )


def generate_report(data):
    """Generate a readable current report in the terminal."""
    print("\n" + "=" * 60)
    print("             STUDENT PRODUCTIVITY REPORT")
    print("=" * 60)

    profile = data.get("profile", {})

    print("\nSTUDENT PROFILE")
    print("-" * 60)

    if profile:
        print(f"Name       : {profile.get('name', '-')}")
        print(f"Semester   : {profile.get('semester', '-')}")
        print(f"Branch     : {profile.get('branch', '-')}")
        print(f"Main Goal  : {profile.get('academic_goal', '-')}")
    else:
        print("Profile not created.")

    print("\nACTIVITY SUMMARY")
    print("-" * 60)

    if data["activities"]:
        count = len(data["activities"])
        total_study = sum(
            float(record.get("study", 0))
            for record in data["activities"]
        )
        total_sleep = sum(
            float(record.get("sleep", 0))
            for record in data["activities"]
        )

        average_study = total_study / count
        average_sleep = total_sleep / count

        print(f"Days recorded     : {count}")
        print(f"Total study hours : {total_study:.2f}")
        print(f"Average study/day : {average_study:.2f}")
        print(f"Average sleep/day : {average_sleep:.2f}")
    else:
        print("No activity records found.")

    print("\nACADEMIC GOALS")
    print("-" * 60)

    if data["goals"]:
        completed = 0

        for goal in data["goals"]:
            progress = float(goal.get("progress", 0))

            if progress >= 100:
                completed += 1

            print(
                f"- {goal.get('title', '-')} : "
                f"{progress:.1f}%"
            )

        print(
            f"\nCompleted goals: {completed}/{len(data['goals'])}"
        )
    else:
        print("No goals found.")

    print("\nREPORT COMPLETE")
