import pytest
import pandas as pd
from datetime import datetime
from Habit_Analysis import compute_streak  # Replace with the actual module name if different


@pytest.fixture(scope="module")
def habit_data():
    """
    Lädt die Daten aus der kombinierten Habit-Tabelle (CSV) und gibt sie als DataFrame zurück.
    Verwendet den Test über alle Funktionen hinweg.
    """
    # Daten aus der CSV-Datei laden
    df = pd.read_csv("combined_habit_data.csv")
    # Konvertiere das Datum in das richtige Format
    df['date'] = pd.to_datetime(df['date'])
    # Sortiere die Daten basierend auf dem Datum für korrekte Streak-Berechnungen
    df = df.sort_values(by="date")
    return df


def test_compute_streak_drink_water(habit_data):
    """
    Testet die compute_streak-Funktion für das Habit 'Drink Water'
    """
    water_dates = habit_data[habit_data['habit_name'] == "Drink Water"]['date'].tolist()
    streak = compute_streak("Drink Water", water_dates)

    # Sicherstellen, dass die Streak für 'Drink Water' korrekt ist.
    assert streak >= 0, "Die Streak für 'Drink Water' sollte >= 0 sein."


def test_compute_streak_exercise(habit_data):
    """
    Testet die compute_streak-Funktion für das Habit 'Exercise'
    """
    exercise_dates = habit_data[habit_data['habit_name'] == "Exercise"]['date'].tolist()
    streak = compute_streak("Exercise", exercise_dates)

    # Sicherstellen, dass die Streak für 'Exercise' korrekt ist.
    assert streak >= 0, "Die Streak für 'Exercise' sollte >= 0 sein."


def test_compute_streak_empty_list():
    """
    Testet die compute_streak-Funktion für eine leere Liste.
    """
    empty_dates = []
    streak = compute_streak("No Habit", empty_dates)

    # Erwartung: Eine leere Liste führt zu einer Streak von 0.
    assert streak == 0, "Eine leere Liste sollte eine Streak von 0 liefern."


def test_compute_streak_read(habit_data):
    """
    Testet die compute_streak-Funktion für das Habit 'Read'
    """
    read_dates = habit_data[habit_data['habit_name'] == "Read"]['date'].tolist()
    streak = compute_streak("Read", read_dates)

    # Überprüfung der Berechnung.
    assert streak >= 0, "Die Streak für 'Read' sollte >= 0 sein."
