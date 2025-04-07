import pandas

data = pandas.read_csv("data/habit_water_tracking.csv")


print(type(data))
print(data)

#data_dict = data.to_dict()
#print(data_dict)

average_amount = data["amount_ml"].mean()
print("the average amount is:", (average_amount))

max_amount = data["amount_ml"].max()
print("the max amount is:", (max_amount))

#Get Data in Row
print(data[data.goal_reached == "Yes"])