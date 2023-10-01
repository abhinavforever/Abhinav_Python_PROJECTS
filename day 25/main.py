# with open("weather_data.csv") as file:
#     data=file.readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temperatures=[]
#     for row in data:
#         if row[1]!='temp':
#             temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas
# data=pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

#data is a dataframe i.e a tabular data structure and a dataframe has .to_dict() method
# data_dict=data.to_dict()
# print(data_dict)

#data["temp"] will return a series i.e. basically a series of temperatures
#a series data structure has .to_list() method which we can use to make a list of the temperatures
# temp_list=data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].max())
# print(data["condition"])
# print(data.condition)

# print(data[data.day=="Monday"])
# print(data[data.temp==data.temp.max()])

# monday=data[data.day=="Monday"]
# print(monday.condition)

#Create a dataframe from scratch

# data_dict={"students":["Amy","James","Angela"],"scores":[76,56,65]}
# data=pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

import pandas

data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count=len(data[data["Primary Fur Color"]=="Gray"])
cinnamon_squirrels_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrels_count=len(data[data["Primary Fur Color"]=="Black"])

data_dict={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[grey_squirrels_count,cinnamon_squirrels_count,black_squirrels_count]
}

df=pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")