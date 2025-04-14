import pandas
from datetime import datetime, timedelta

# Data is based on one month for the habit Drink, Exercise, Meditation, Read, Sleep, (new added habits by user)
data = pandas.read_csv("data/combined_habit_data.csv")
#print(data)

data.shape
print("data shape: ",data.shape)

data.count()
print("data count: ", data.count())

# HABIT COUNT TABLE: Counts dates of: Drink, Exercise, Meditation, Read, Sleep, (new added habits by user)
data.groupby("habit_name").count()
print("data group by : ", data.groupby("habit_name").count())

# HABIT SUM TABLE: Sums up the amount of: Drink, Exercise, Meditation, Read, Sleep, (new added habits by user)
data.groupby("habit_name").sum("amount")
print(data.groupby("habit_name").sum("amount"))

# GOAL REACHED TABLE per habit count: Drink, Exercise, Meditation, Read, Sleep, (new added habits by user)
pivot_goal_count_df = data.pivot_table(index="habit_name", columns="goal_reached", values="date", aggfunc="count").fillna(0).astype(int).astype(str) + ""
print(pivot_goal_count_df)

# AVERAGE AMOUNT TABLE: Average amount per habit: Drink, Exercise, Meditation, Read, Sleep, (new added habits by user)
pivot_goal_avg_df = data.pivot_table(index="habit_name", columns="goal_reached", values="amount", aggfunc="mean").fillna(0).astype(int).astype(str) + ""
print(pivot_goal_avg_df)

# AVERAGE AMOUNT TABLE
pivoted_df = data.pivot_table(index="goal_reached", columns="habit_name", values="amount")
print(pivoted_df)


#DATA COUNT: SUM AND AVERAGE per habit

#WATER
water_habit_sum = (data[data["habit_name"] == "Drink Water"].sum()["amount"])
print("water sum:", water_habit_sum)
water_habit_avg = water_habit_sum/len(data[data["habit_name"] == "Drink Water"])
print("water avg:", water_habit_avg)

#EXERCISE
exercise_habit_sum = (data[data["habit_name"] == "Exercise"].sum()["amount"])
print("exercise sum:", exercise_habit_sum)
exercise_habit_avg = exercise_habit_sum/len(data[data["habit_name"] == "Exercise"])
print("exercise avg:", exercise_habit_avg)

#MEDITATION
meditation_habit_sum = (data[data["habit_name"] == "Meditation"].sum()["amount"])
print("meditation sum:", meditation_habit_sum)
meditation_habit_avg = meditation_habit_sum/len(data[data["habit_name"] == "Meditation"])
print("meditation avg:", meditation_habit_avg)

#SLEEP
sleep_habit_sum = (data[data["habit_name"] == "Sleep"].sum()["amount"])
print("sleep sum:", sleep_habit_sum)
sleep_habit_avg = sleep_habit_sum/len(data[data["habit_name"] == "Sleep"])
print("sleep avg:", sleep_habit_avg)


#READ
read_habit_sum = (data[data["habit_name"] == "Read"].sum()["amount"])
print("read sum:", read_habit_sum)
read_habit_avg = read_habit_sum/len(data[data["habit_name"] == "Read"])
print("read avg:", read_habit_avg)


#DATA COUNT per habit
water_habit_len = len(data[data["habit_name"] == "Drink Water"])
exercise_habit_len = len(data[data["habit_name"] == "Exercise"])
meditation_habit_len = len(data[data["habit_name"] == "Meditate"])
sleep_habit_len = len(data[data["habit_name"] == "Sleep 7+ Hours"])
read_habit_len = len(data[data["habit_name"] == "Read"])
print("water count:", water_habit_len)
print("exercise count:", exercise_habit_len)
print("meditation count:", meditation_habit_len)
print("sleep count:", sleep_habit_len)
print("read count:", read_habit_len)




## STREAK COMPUTATION

# Streak computation function

def compute_streak(habit_name, dates):
    """
    Compute the longest streak for a given habit.

    :param habit_name: Name of the habit
    :param dates: List of dates when the habit was completed (datetime objects)
    :return: Longest streak length (int)
    """
    # Sort the dates
    sorted_dates = sorted(dates)

    # If no dates are provided, the streak is 0
    if not sorted_dates:
        print(f"Habit '{habit_name}': No completion dates found.")
        return 0

    # Initialize streaks
    longest_streak = 1
    current_streak = 1

    # Calculate the streak
    for i in range(1, len(sorted_dates)):
        # Check if the difference is exactly one day
        if sorted_dates[i] - sorted_dates[i - 1] == timedelta(days=1):
            current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        else:
            current_streak = 1

    # Output the longest streak
    print(f"Habit '{habit_name}': Longest Streak = {longest_streak}")
    return longest_streak


# Load the habit data CSV
csv_file = 'data/combined_habit_data.csv'
habit_data = pandas.read_csv(csv_file)

# Convert the date column to datetime
habit_data['date'] = pandas.to_datetime(habit_data['date'])

# Loop through each habit and compute streak
unique_habits = habit_data['habit_name'].unique()
streak_results = {}

for habit in unique_habits:
    # Filter rows for the current habit
    habit_dates = habit_data[habit_data['habit_name'] == habit]['date']

    # Pass dates to the compute_streak function
    streak_results[habit] = compute_streak(habit, habit_dates)

# Print all streak results
print("\nStreak Results:")
for habit, streak in streak_results.items():
    print(f"{habit}: {streak}")

"""
data_dict = {
    "Habit": ["Exercise", "Meditate", "Sleep" ,"Read"],
    "Count": [exercise_habit_len, meditation_habit_len, sleep_habit_len, read_habit_len],
    "Average": [exercise_habit_avg, meditation_habit_avg, sleep_habit_avg, read_habit_avg]
}

print(data_dict)


df = pandas.DataFrame(data_dict)
df.to_csv("habit_count.csv")

pivoted_df = df.pivot(index="Habit", columns="Count", values="Average")
print(pivoted_df)


average_amount = data["amount"].mean()
#print("the average amount is:", (average_amount))

max_amount = data["amount"].max()
#print("the max amount is:", (max_amount))
"""