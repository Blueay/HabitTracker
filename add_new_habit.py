#HABIT Tracker - dfjior
# TEST

class Habit:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount


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
                print(f"{i}. Date: {habit.date}, Description: {habit.description}, Amount: {habit.amount:.2f}")

    def total_habit(self):
        total = sum(habit.amount for habit in self.habit)
        print(f"Total habit: {total: .2f}")




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
            description = input ("Enter the description: ")
            amount = float(input("Enter the amount: "))
            habit = Habit(date, description, amount)
            tracker.add_habit(habit)
            print("Habit added successfully.")
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

