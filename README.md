# Student Productivity Simulator & Academic Life Analyzer

## Overview

The Student Productivity Simulator is a terminal-based Python
application designed to help students record their daily activities,
manage academic goals, analyze their routine, and explore possible
changes to their schedule.

The project uses simple Python concepts such as functions, loops,
conditional statements, lists, dictionaries, file handling, JSON, and
There is exception handling and the data is stored in a JSON file locally.
The information is still accessible when the program is next opened.

The application is rule-based and is intended for personal academic
Planning and routine analysis; it does not pretend to be scientific
measure productivity.

## Features

-   Student profile management
-   Daily activity and time tracking
-   Add, view, edit, and delete activity records
-   Daily routine analysis
-   Academic goal management
-   Goal progress tracking
-   What-if routine simulation
-   Progress history
-   Text-based report generation
-   Persistent data storage using JSON
-   Input validation and error handling

## Technologies Used

-   Python 3
-   JSON
-   Python Standard Library
-   `datetime` for date validation and calculations
-   Terminal / Command Prompt

There is no need to use any external Python packages.

## Project Structure

``` text
student-productivity-simulator/
│
├── data/
│   └── student_data.json
│
├── activities.py
├── analysis.py
├── goals.py
├── main.py
├── profile.py
├── reports.py
├── simulator.py
│
├── README.md
└── statement.md
```

### File Description

  File                       Purpose
  -------------------------- --------------------------------------------------
  The main.py file serves as the main entry point and contains the menu for the application.
  profile.py               Creates, displays, and modifies the student profile
  The file `activities.py` keeps record of and handles daily activities.
  The program called analysis.py examines the student's recorded routine.
  `goals.py`                 Creates and manages academic goals.
  `simulator.py` is a program which simulates changes to a daily routine
  `reports.py` shows the history and produces reports
  `data/student_data.json`   Keeps project data permanently
  statement.md contains the project's problem statement and scope

## How to Run

1. Open the project folder using VS Code, the Command Prompt, or PowerShell.
In the folder of the project open the terminal and ensure that main.py is there.
3.  Run:

``` bash
python main.py
```

Important: The only file that should be run directly is main.py.
The other Python files are internal modules used by main.py.

## Data Storage

The application stores information in:

``` text
data/student_data.json
```

The program creates the required data folder/file when needed and saves
Changes to the JSON file.

## Basic Usage

After starting the program, the main menu provides:

1.  Student Profile
2.  Daily Activity Tracker
3.  Analyze My Day
4.  Academic Goals
5.  Routine Simulator
6.  Progress History
7.  Generate Report
8.  Exit

## Validation and Error Handling

The application handles common invalid inputs such as invalid menu
choices, empty text input, invalid dates, negative activity hours,
invalid goal progress, duplicate activity dates, daily activity totals
More than 24 hours, and with missing or invalid data that was saved.

## Testing

The project should be tested through its main features, including
profile management, activity records, daily analysis, academic goals,
routine simulation, progress history, report generation, JSON
The handling of invalid input and persistence after restarting.

## Future Enhancements

Possible improvements include weekly and monthly analysis, detailed goal
statistics, report export, graphical time-use representation, academic
Reminders and more sophisticated scheduling features.
