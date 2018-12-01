import os
import csv

csvpath=os.path.join('.','PyBank', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)
    print(f"{csv_header}")
    for row in csvreader:
        print(row)#first 2 rows