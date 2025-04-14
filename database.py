import pandas as pd

def load_and_combine_data():

    # Read the csv.file that was created by add_new_habit.py
    habits_file = "data/habits.csv"

    # Read the csv.file from the backup as habit_tracking_history_backup.csv
    backup_file = "data/habit_tracking_history_backup.csv"

    # Read both files as data frames
    habits_data = pd.read_csv(habits_file)
    backup_data = pd.read_csv(backup_file)


    # Combine both data from the add_new_habit and from the backup history
    combined_data = pd.concat([habits_data, backup_data], ignore_index=True)
    print("Combined Data:")
    print(combined_data)

    return habits_data, backup_data, combined_data


if __name__ == "__main__":
    habits, backup, combined = load_and_combine_data()

    print("\nHabits Data:")
    print(habits)

    print("\nBackup Data:")
    print(backup)

    print("\nCombined Data (Habits + Backup):")
    print(combined)


    print(type(combined))
    print(combined)

# Convert into dictionary
#data_dict = combined.to_dict()
#print(data_dict)

# selected filtered data (optional) as SELECTED TABLE
    print(combined[combined["habit_name"] == "Exercise"])

#Get combined data in Row
    print(combined[combined.goal_reached == "True"])


# Safe the combined Data as a DataFrame in combined new data file:

    combined.to_csv("data/combined_habit_data.csv", index=False)

