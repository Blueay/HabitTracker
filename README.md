# HabitTracker

Hello!

I built this app while learning Object Oriented and Functional Programming with Python and working on an assignment at IU University in April 2025. Luckily, I had some help from ChatGPT—which made learning to code (and getting things to actually work) a lot easier and more fun.

The app isn’t fully finished yet—things like a proper GUI and bonus points are still on the to-do list. But overall, it was a cool little project to dive into, and I learned a lot along the way.


------
## All-in-All
A data-driven habit tracking application designed to help users build, analyze,
and improve their habits over time. The Habit Tracker monitors habits, provides analytical insights,
and allows user-friendly data management.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Application Architecture](#application-architecture)
- [Module Overview](#module-overview)
  - [Main Script (`main.py`)](#main-script-mainpy)
  - [Habit Management (`add_new_habit.py`)](#habit-management-add_new_habitpy)
  - [Data Management (`download_csv.py`)](#data-management-download_csvpy)
  - [Analysis Module (`Habit_Analysis.py`)](#analysis-module-habit_analysispy)
- [Tests (`test_habit_analysis.py`)](#tests-test_habit_analysispy)
- [Application Architecture](#application-architecture)
- [Concept](#concept)
- [Key Features](#key-features)
- [Conclusion](#conclusion)

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install the required dependencies:
   ```bash
   pip install pandas
   ```
3. Make sure the folder structure is as follows:
   ```
   data/
     - habits.csv
     - habit_tracking_history_backup.csv
   main.py
   add_new_habit.py
   database.py
   habit_analysis.py
   test_habit_analysis.py
   ```

---

## Usage

To run the program, execute the main script:

```bash
python main.py
```

The program provides a menu with the following features:
1. **Manage Habits**: Add new habits, remove existing ones, and view saved habits.
2. **Load and Combine Data**: Import CSV data and combine it for analysis.
3. **Analyze Data**: Get insights such as streak calculations, averages, and total amounts.
4. **Exit**: Quit the application.

Follow the prompts after selecting a menu option to perform the desired action.


## Application Architecture

The Habit Tracker application is designed with a modular architecture to ensure simplicity, scalability, and 
maintainability. Each module handles a specific aspect of functionality, making it easier to extend and debug.
The architecture can be visualized as follows:
                                   +----------------------------+
                                           | main.py |
                                   +----------------------------+
                                               |
        +------------------------+-------------------------------+--------------------------+
        |                        |                               |                          |
 +------------------+    +------------------------+    +-----------------------+    +-----------------------+
 | add_new_habit.py |    | database.py            |    | habit_analysis.py     |    | test.py               |
 |                  |    |                        |    |                       |    |                       |
 | add_habit()      |    | load_data()            |    | data.shape()          |    | test.continuous_dates |    
 | remove_habit()   |    | combine_dataframe()    |    | data.count()          |    | test.consecutive_dates|
 | view_habit()     |    | selected_table()       |    | data.groupby()        |    | test.empty_dates      |
 | total_habit()    |    |                        |    | pivot.goal.count()    |    | test.table_creation   |
 | save_to_csv      |    |                        |    | pivot.goal.avg()      |    | test.data_group_sum   |
 |                  |    |                        |    | streak.computation()  |    | test.streak_habit     |
 +------------------+    +------------------------+    +-----------------------+    +-----------------------+

---

## Module Overview

The application is modular and consists of independent components that work together seamlessly:

### Main Script (`main.py`)
This is the core control and entry point of the application. It includes:

- **`display_menu()`**: Displays the main menu to the user.
- **`habit_tracker_menu()`**: Enables the user to add, remove, view, and manage habits.
- **`analysis_menu()`**: Allows the user to analyze habits, calculate streaks, and view aggregate statistics.
- **`main()`**: Orchestrates the menu and routes functionality to respective modules.

---

### Habit Management (`add_new_habit.py`)

Defines the functionality for managing individual habits, including:
- **Class `Habit`**: Represents a single habit with attributes like date, habit name, amount, and goal completion status.
- **Class `HabitTracker`**: Manages the collection of habits and provides methods to:
  - `add_habit()`: Add a new habit.
  - `remove_habit()`: Remove an existing habit.
  - `view_habit()`: Display all stored habits.
  - `save_to_csv()`: Save the habits to a CSV file for later reference.

Habit Management ensures a structured and easy way to keep track of user-defined habits.

---

### Data Management (`database.py`)

Manages data import and integration from CSV files:
- **`load_and_combine_data()`**: Reads `habits.csv` (current habits) and `habit_tracking_history_backup.csv` (backup), merges them into a single dataset, and returns it as a Pandas DataFrame.
- Saves the combined data into a new file, `combined_habit_data.csv`.

Core functionality includes:
- Calculating averages and maximum values.
- Filtering data for specific habits (e.g., "Exercise").
- Efficient merging of habit data for long-term tracking.

---

### Analysis Module (`habit_analysis.py`)

Provides advanced analytics for habits:
- **`compute_streak(habit, habit_dates)`**: Computes streaks for habits (i.e., the longest consecutive days a habit is completed).
- Calculates aggregate sums, averages, and filtered datasets for individual or grouped habits (e.g., "Meditation").
- Identifies goal completion trends across all recorded habits.

This module adds data-driven insights for better habit formation and monitoring.

---

## Tests (`test_habit_analysis.py`)

The test suite ensures the correctness and reliability of the Habit Tracker's analytics. It focuses on the core functions of streak calculation, data aggregation, and summary statistics. Below are the main components of the test file:

- **`habit_data()`**: Generates mock data for testing purposes.
- **`test_compute_streak_with_continuous_dates()`**: Validates streak calculations for continuous (consecutive) habit dates.
- **`test_compute_streak_with_non_consecutive_dates()`**: Ensures streaks are calculated correctly when habit dates are not consecutive.
- **`test_compute_streak_with_empty_dates()`**: Checks streak computation with an empty set of dates.
- **`test_pivot_table_creation()`**: Tests the creation of pivot tables for habit summaries.
- **`test_data_grouping_and_summary()`**: Verifies that data grouping and summary statistics (totals, averages) run correctly.
- **`test_streak_from_habit_data()`**: End-to-end test to verify streak analytics directly from habit data.

To run the tests, you can use Python's built-in unittest framework or another testing tool like `pytest`:

```bash
python -m unittest test_habit_analysis.py
```

These tests ensure the robustness of all analytical features.

---
