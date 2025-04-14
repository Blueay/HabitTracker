import pytest
import pandas as pd
from datetime import datetime, timedelta
from habit_analysis import compute_streak  # Import the function to test


# Mock data for testing
@pytest.fixture
def habit_data():
    """
    Fixture to provide mock habit data for testing.
    """
    return pd.DataFrame({
        "habit_name": [
            "Drink Water", "Drink Water", "Exercise", "Meditation",
            "Drink Water", "Exercise", "Meditation", "Read"
        ],
        "date": [
            "2023-10-01", "2023-10-02", "2023-10-01", "2023-10-05",
            "2023-10-03", "2023-10-02", "2023-10-06", "2023-10-07"
        ],
        "amount": [500, 700, 30, 20, 600, 40, 25, 5],
        "goal_reached": [True, True, False, True, False, True, False, True],
    })


def test_compute_streak_with_continuous_dates():
    """
    Test the compute_streak function with continuous dates.
    """
    habit_name = "Drink Water"
    dates = [
        datetime(2023, 10, 1),
        datetime(2023, 10, 2),
        datetime(2023, 10, 3),
    ]
    assert compute_streak(habit_name, dates) == 3  # Longest streak is 3 days


def test_compute_streak_with_non_consecutive_dates():
    """
    Test the compute_streak function with non-consecutive dates.
    """
    habit_name = "Drink Water"
    dates = [
        datetime(2023, 10, 1),
        datetime(2023, 10, 3),
        datetime(2023, 10, 5),
    ]
    assert compute_streak(habit_name, dates) == 1  # Longest streak is 1 day


def test_compute_streak_with_empty_dates():
    """
    Test the compute_streak function with no dates.
    """
    habit_name = "Drink Water"
    dates = []
    assert compute_streak(habit_name, dates) == 0  # No streaks possible


def test_pivot_table_creation(habit_data):
    """
    Test the creation of pivot tables for goal counts and averages.
    """
    # Convert the 'date' column to datetime for proper operations
    habit_data['date'] = pd.to_datetime(habit_data['date'])

    # Calculate a pivot for goal counts
    pivot_goal_count_df = habit_data.pivot_table(
        index="habit_name", columns="goal_reached", values="date", aggfunc="count"
    ).fillna(0).astype(int)

    # Check that the pivot table is created correctly
    assert pivot_goal_count_df.loc["Drink Water", True] == 2
    assert pivot_goal_count_df.loc["Exercise", False] == 1
    assert pivot_goal_count_df.loc["Meditation", True] == 1

    # Calculate a pivot for goal averages
    pivot_goal_avg_df = habit_data.pivot_table(
        index="habit_name", columns="goal_reached", values="amount", aggfunc="mean"
    ).fillna(0).astype(float)

    # Check some calculated averages
    assert pivot_goal_avg_df.loc["Drink Water", True] == 600
    assert pivot_goal_avg_df.loc["Exercise", True] == 40


def test_data_grouping_and_summary(habit_data):
    """
    Test the grouping of habit data and summary statistics.
    """
    # Convert the 'date' column to datetime for grouping
    habit_data['date'] = pd.to_datetime(habit_data['date'])

    # Group by habit name and sum up "amount"
    grouped_sum = habit_data.groupby("habit_name").sum(numeric_only=True)
    assert grouped_sum.loc["Drink Water", "amount"] == 1800
    assert grouped_sum.loc["Exercise", "amount"] == 70

    # Group by habit name and count the occurrences
    grouped_count = habit_data.groupby("habit_name").count()
    assert grouped_count.loc["Drink Water", "date"] == 3
    assert grouped_count.loc["Meditation", "date"] == 2


def test_streak_from_habit_data(habit_data):
    """
    Test streak computation for habits present in the mock data.
    """
    # Convert the 'date' column to datetime
    habit_data['date'] = pd.to_datetime(habit_data['date'])

    # Extract unique habits
    unique_habits = habit_data['habit_name'].unique()

    # Initialize streak results
    streak_results = {}

    # Calculate streaks for each habit
    for habit in unique_habits:
        habit_dates = habit_data[habit_data['habit_name'] == habit]['date']
        streak_results[habit] = compute_streak(habit, habit_dates)

    # Expected results
    assert streak_results["Drink Water"] == 3
    assert streak_results["Exercise"] == 2
    assert streak_results["Meditation"] == 2
    assert streak_results["Read"] == 1
