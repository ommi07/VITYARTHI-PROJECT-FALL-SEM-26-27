# Project Statement

## Project Title

**Student Productivity Simulator & Academic Life Analyzer**

## Problem Statement

Students divide their time among activities such as classes, self-study,
sleep, exercise, entertainment, travel, and other daily
responsibilities. Without recording this information, it can be
difficult to understand how available time is being distributed or to
compare an actual routine with academic goals.

The Student Productivity Simulator provides a simple terminal-based
system where a student can record daily activities, manage academic
goals, analyze a recorded routine, and simulate possible changes to the
routine.

The application is intended as a simple planning and analysis tool. Its
analysis is rule-based and does not claim to scientifically measure a
student's productivity.

## Scope

The project covers:

-   Maintaining a basic student profile
-   Recording daily activities and time spent on them
-   Viewing, editing, and deleting activity records
-   Analyzing the distribution of time in a selected day
-   Creating and tracking academic goals
-   Simulating changes to a daily routine
-   Viewing progress history
-   Generating text-based reports
-   Storing information locally using JSON

The project operates entirely through the terminal and does not require
an internet connection or external services.

## Target Users

The primary target users are students who want a simple way to record
their daily routine and academic goals and review how their time is
being used.

## High-Level Features

### 1. Student Profile Management

The user can create, view, and update basic profile information.

### 2. Daily Activity Tracker

The user can record activities such as study, classes, sleep, exercise,
entertainment, social activities, travel, and other activities.

### 3. Routine Analysis

The system analyzes a selected day's recorded activities and provides
simple rule-based observations about time usage.

### 4. Academic Goal Management

The user can create academic goals, set targets or deadlines, and update
progress.

### 5. Routine Simulator

The user can change the duration of an activity and compare the
simulated routine with the original routine.

### 6. Progress History

The user can review previously recorded activity and goal information.

### 7. Report Generation

The system can display a text-based summary of the student's recorded
information.

### 8. Persistent Data Storage

Profile information, activities, and goals are stored in a JSON file so
that the data remains available when the application is reopened.

## Project Execution

The complete application is started by running:

``` bash
python main.py
```

`main.py` acts as the main entry point and connects the other Python
modules of the project.
