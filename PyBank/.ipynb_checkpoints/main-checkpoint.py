import os
import csv

Data=os.path.join('..','PyBank', 'budget_data.csv')
Date=[]
PL=[]
Change=[]

with open(Data, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)
    #print(f"{csv_header}")
    for row in csvreader:
        Date.append(row[0])
        PL.append(int(row[1]))
        
Data_Cleaned=zip(Date,PL)

print("Financial Analysis")
print("--------------------------------")
print (f"Total Months: {len(Date)}")
def fsum(List):
    Sum = 0
    for i in List:
        Sum = Sum + i
    return Sum
print (f"Total: {fsum(PL)}")
Change=[PL[i+1]-PL[i] for i in range(len(PL)-1)]
print (f"Average  Change: {round(sum(Change)/len(Change),2)}")
print (f"Greatest Increase in Profits: {Date[Change.index(max(Change))+1]} {max(Change)}")
print (f"Greatest Decrease in Profits: {Date[Change.index(min(Change))+1]} {min(Change)}")



output_file=os.path.join("budget_final.txt")
with open(output_file, "w", newline="\n") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("------------------------------------\n")
    text_file.write(f"Total Months: {len(Date)}\n")
    text_file.write(f"Total: {fsum(PL)}\n")
    text_file.write(f"Average  Change: {round(sum(Change)/len(Change),2)}\n")
    text_file.write(f"Greatest Increase in Profits: {Date[Change.index(max(Change))+1]} {max(Change)}\n")
    text_file.write(f"Greatest Decrease in Profits: {Date[Change.index(min(Change))+1]} {min(Change)}\n")