from add_new_habit import Habit, HabitTracker
from database import load_and_combine_data
from habit_analysis import compute_streak
import pandas as pd


# Funktion zur Anzeige des Hauptmenüs
def display_menu():
    print("\nHabit Tracker Main Menu:")
    print("1. Add and Manage Habits")
    print("2. Load and Combine Habit Data")
    print("3. Analyze Habit Data")
    print("4. Exit")


# Menü für das Hinzufügen und Verwalten von Gewohnheiten
def habit_tracker_menu(tracker):
    while True:
        print("\nHabit Management Menu:")
        print("1. Add Habit")
        print("2. Remove Habit")
        print("3. View Habits")
        print("4. Total Habit Amount")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Hinzufügen neuer Gewohnheiten
            date = input("Enter the date (YYYY-MM-DD): ")
            habit_name = input("Enter the habit name: ")
            amount = float(input("Enter the amount: "))
            goal_reached = input("Is the goal reached? (yes/no): ").lower() == "yes"
            habit = Habit(date, habit_name, amount, goal_reached)
            tracker.add_habit(habit)
            print("Habit added successfully.")
            tracker.save_to_csv()

        elif choice == "2":
            # Entfernen einer bestehenden Gewohnheit
            index = int(input("Enter the habit index to remove: ")) - 1
            tracker.remove_habit(index)

        elif choice == "3":
            # Ansicht der bisherigen Gewohnheiten
            tracker.view_habit()

        elif choice == "4":
            # Ausgabe der Gesamtsumme aller Aktivitäten
            tracker.total_habit()

        elif choice == "5":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice. Please try again.")


# Menü für die Analyse von Gewohnheiten
def analysis_menu(combined_data):
    while True:
        print("\nHabit Analysis Menu:")
        print("1. Compute Habit Streaks")
        print("2. Analyze Goals and Statistics")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Berechnung der Gewohnheitsserien
            habit_names = combined_data["habit_name"].unique()
            combined_data["date"] = pd.to_datetime(combined_data["date"])

            print("\nStreak Analysis:")
            for habit in habit_names:
                habit_dates = combined_data[combined_data["habit_name"] == habit]["date"]
                streak = compute_streak(habit, habit_dates)
                print(f"- {habit}: Longest streak is {streak} days")

        elif choice == "2":
            # Analyse von Zielen und Statistiken
            print("\nGoals and Statistics:")
            total = combined_data.groupby("habit_name")["amount"].sum()
            average = combined_data.groupby("habit_name")["amount"].mean()
            print("Habit Totals:\n", total)
            print("\nHabit Averages:\n", average)

        elif choice == "3":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice. Please try again.")


# Hauptfunktion
def main():
    tracker = HabitTracker()
    combined_data = None  # Platzhalter für kombinierte Daten

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # Menü für die Verwaltung von Gewohnheiten
            habit_tracker_menu(tracker)

        elif choice == "2":
            print("\nLoading and Combining Habit Data...")
            try:
                # Methode zum Laden und Kombinieren von Daten aufrufen
                habits_data, backup_data, combined_data = load_and_combine_data()
                print("Data loaded and combined successfully!")

                # Optional: Vorschau der kombinierten Daten anzeigen
                print("\nPreview of Combined Data:")
                print(combined_data.head())

            except Exception as e:
                print(f"Failed to load data: {e}")

        elif choice == "3":
            if combined_data is not None:
                # Menüs für die Analyse der Gewohnheiten, falls Daten verfügbar sind
                analysis_menu(combined_data)
            else:
                print("You need to load and combine the data first (Menu Option 2).")

        elif choice == "4":
            # Beendigung des Programms
            print("Goodbye! Exiting the Habit Tracker.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
