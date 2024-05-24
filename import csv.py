import csv      


  # Create a CSV reader object
#reader = csv.reader('tasks.csv', delimiter=",") 

with open('tasks.csv', 'r', newline='') as csvfile:
    for row in csvfile:
        print(row)