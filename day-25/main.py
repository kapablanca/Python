# with open("weather_data.csv") as file:
#     data = file.readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# print(data["temp"].mean())

# max_temperature = data["temp"].max()


#Get data in column
# print(data["condition"])
# print(data.condition)

#Get data in rows
# print(data[data.day == "Monday"])

# print(data[data["temp"] == data.temp.max()])

# monday = data[data.day == "Monday"]
#
# print((monday.temp *(9/5) + 32))

#Create a dataframe from scratch
# data_dict = {
#     "students":["Amy","James","Angela"],
#     "scores":[76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

data = pandas.read_csv("squirrel_count.csv")
# fur_color = data.groupby("Primary Fur Color")[["Primary Fur Color"]].count()
# fur = fur_color.transform("count")

# grouped = data.groupby("Primary Fur Color")
# count = grouped.size()

fur = data["Primary Fur Color"]
new = fur.value_counts().reset_index()

print(new)



















