import csv
filepath = '/Users/charanjeetsingh/Documents/PythonProjects/Python_ Experiments/files/weather.csv'

with open(filepath, 'r') as file:
    file = list(csv.reader(file))
    for row in file:
        print(row)

city = input("Enter City: ")

for row in file[1:]:
    if city == row[0]:
        print(row[1])
