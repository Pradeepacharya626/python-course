                      #DAY 15

# csv module
import csv               

with open("weather.csv",'r') as file :
  data = list(csv.reader(file))

# print(data)

village = input("Enter a village")

for row in data :
  if row[0] == village :
    print(row[1])