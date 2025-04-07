import pandas

data = pandas.read_csv("data/habit_tracking_extended.csv")
#print(data)

data.shape
print("data shape: ",data.shape)

data.count()
print("data count: ", data.count())

data.groupby("habit").count()
print("data group by : ", data.groupby("habit").count())

data.groupby("habit").sum("amount")
print(data.groupby("habit").sum("amount"))

pivot_goal_count_df = data.pivot_table(index="habit", columns="goal_reached", values="date", aggfunc="count").fillna(0).astype(int).astype(str) + ""
print(pivot_goal_count_df)

pivot_goal_avg_df = data.pivot_table(index="habit", columns="goal_reached", values="amount", aggfunc="mean").fillna(0).astype(int).astype(str) + "ml"
print(pivot_goal_avg_df)

pivoted_df = data.pivot_table(index="goal_reached", columns="habit", values="amount")
print(pivoted_df)


#DATA COUNT


water_habit_sum = (data[data["habit"] == "Drink Water"].sum()["amount"])
print("water sum:", water_habit_sum)
water_habit_avg = water_habit_sum/len(data[data["habit"] == "Drink Water"])
print("water avg:", water_habit_avg)


exercise_habit_sum = (data[data["habit"] == "Exercise"].sum()["amount"])
print("exercise sum:", exercise_habit_sum)
exercise_habit_avg = exercise_habit_sum/len(data[data["habit"] == "Exercise"])
print("exercise avg:", exercise_habit_avg)

meditation_habit_sum = (data[data["habit"] == "Meditate"].sum()["amount"])
print("meditation sum:", meditation_habit_sum)
meditation_habit_avg = meditation_habit_sum/len(data[data["habit"] == "Meditate"])
print("meditation avg:", meditation_habit_avg)

sleep_habit_sum = (data[data["habit"] == "Sleep 7+ Hours"].sum()["amount"])
print("sleep sum:", sleep_habit_sum)
sleep_habit_avg = sleep_habit_sum/len(data[data["habit"] == "Sleep 7+ Hours"])
print("sleep avg:", sleep_habit_avg)

read_habit_sum = (data[data["habit"] == "Read"].sum()["amount"])
print("read sum:", read_habit_sum)
read_habit_avg = read_habit_sum/len(data[data["habit"] == "Read"])
print("read avg:", read_habit_avg)



#water_habit_avg = (data[data["habit"] == "Drink Water"].mean()["amount"])



water_habit_len = len(data[data["habit"] == "Drink Water"])
exercise_habit_len = len(data[data["habit"] == "Exercise"])
meditation_habit_len = len(data[data["habit"] == "Meditate"])
sleep_habit_len = len(data[data["habit"] == "Sleep 7+ Hours"])
read_habit_len = len(data[data["habit"] == "Read"])
print("water count:", water_habit_len)
print("exercise count:", exercise_habit_len)
print("meditation count:", meditation_habit_len)
print("sleep count:", sleep_habit_len)
print("read count:", read_habit_len)



data_dict = {
    "habit": ["Exercise", "Meditate", "Sleep 7+ Hours" ,"Read"],
    "Count": [exercise_habit_len, meditation_habit_len, sleep_habit_len, read_habit_len],
    "Average": [exercise_habit_avg, meditation_habit_avg, sleep_habit_avg, read_habit_avg]
}

print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("habit_count.csv")

pivoted_df = df.pivot(index="habit", columns="Count", values="Average")
print(pivoted_df)


average_amount = data["amount"].mean()
#print("the average amount is:", (average_amount))

max_amount = data["amount"].max()
#print("the max amount is:", (max_amount))



"""
#Get Data in Row
water_habit = print(data[data.habit == "Drink Water"])
water_habit_count = data[data.habit == "Drink Water"].count()
water_habit_len = len(data[data["habit"] == "Drink Water"])

#print(water_habit)
print(water_habit_count)
print(water_habit_len)


exercise_habit = print(data[data.habit == "Exercise"])
exercise_habit_count = data[data.habit == "Exercise"].count()
exercise_habit_len = len(data[data["habit"] == "Exercise"])

#print(exercise_habit)
print(exercise_habit_count)
print(exercise_habit_len)

meditation_habit = print(data[data.habit == "Meditate"])
meditation_habit_count = data[data.habit == "Meditate"].count()
meditation_habit_len = len(data[data["habit"] == "Meditate"])

#print(meditation_habit)
print(meditation_habit_count)
print(meditation_habit_len)



sleep_habit = print(data[data.habit == "Sleep 7+ Hours"])
sleep_habit_count = data[data.habit == "Sleep 7+ Hours"].count()
sleep_habit_len = len(data[data["habit"] == "Sleep 7+ Hours"])

#print(sleep_habit)
print(sleep_habit_count)
print(sleep_habit_len)

read_habit = print(data[data.habit == "Read"])
read_habit_count = data[data.habit == "Read"].count()
read_habit_len = len(data[data["habit"] == "Read"])

#read_habit = print(data[data.habit == "Read"])

"""