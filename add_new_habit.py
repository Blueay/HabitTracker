#HABIT Tracker - dfjior
# TEST

import csv


class Habit:
    def __init__(self, date, habit_name, amount, goal_reached=False):
        self.date = date
        self.habit_name = habit_name
        self.amount = amount
        self.goal_reached = goal_reached


class HabitTracker:
    def __init__(self):
        self.habit = []

    def add_habit(self, expense):
        self.habit.append(expense)

    def remove_habit(self, index):
        if 0 <= index < len(self.habit):
            del self.habit[index]
            print("Habit removed successfully.")
        else:
            print("Invalid habit index.")

    def view_habit(self):
        if len(self.habit) == 0:
            print("No habit found.")
        else:
            print("Habit List:")
            for i, habit in enumerate(self.habit, start=1):
                print(f"{i}. date: {habit.date}, habit_name: {habit.habit_name}, Amount: {habit.amount:.2f}, goal_reached: {habit.goal_reached}")

    def total_habit(self):
        total = sum(habit.amount for habit in self.habit)
        print(f"Total habit: {total: .2f}")

    def save_to_csv(self, filename="data/habits.csv"):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "habit_name", "amount", "goal_reached"])  # Header
            for habit in self.habit:
                writer.writerow([habit.date, habit.habit_name, habit.amount, habit.goal_reached])
        print(f"Habits saved to {filename}.")




def main():
    tracker = HabitTracker()

    while True:
        print("\nHabit Tracker Menu:")
        print("1. Add Habit")
        print("2. Remove Habit")
        print("3. View Habit")
        print("4. Total Habit")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            habit_name = input ("Enter the habit name: ")
            amount = float(input("Enter the amount: "))
            goal_reached = bool(input("Is the goal reached? (yes/no): "))
            habit = Habit(date, habit_name, amount,goal_reached)
            tracker.add_habit(habit)
            print("Habit added successfully.")
            tracker.save_to_csv()

        elif choice == "2":
            index = int(input("Enter the habit index to remove: ")) - 1
            tracker.remove_habit(index)
        elif choice == "3":
            tracker.view_habit()
        elif choice == "4":
            tracker.total_habit()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




