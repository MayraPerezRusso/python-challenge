import os
import csv

Data=os.path.join('..','PyPoll', 'election_data.csv')
ID=[]
County=[]
Candidatelist=[]

with open(Data, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)
    for row in csvreader:
        ID.append(int(row[0]))
        County.append(row[1])
        Candidatelist.append(row[2])
        
print("Election Results")
print("--------------------------------")
print (f"Total Votes: {len(ID)}")
print("--------------------------------")

def Candidate(list1): 
    final_list = [] 
    for i in list1: 
        if i not in final_list: 
            final_list.append(i) 
    return final_list
FinalCand=[]
FinalCand=Candidate(Candidatelist)

def analysis(Candi):
    for i in Candi:
        name=Candi
        pct="{:.3%}".format(Candidatelist.count(Candi)/len(ID))
        count=Candidatelist.count(Candi)
    return f"{name}: {pct} {count}"
name1=[]
count1=[]
for i in FinalCand:
    print(analysis(i))
    name1.append(i)
    count1.append(Candidatelist.count(i))
    
print("--------------------------------")
print (f"Winner: {name1[count1.index(max(count1))]}")
print("--------------------------------")

output_file=os.path.join("election_final.txt")
with open(output_file, "w", newline="\n") as text_file:
    text_file.write("Election Results\n")
    text_file.write("------------------------------------\n")
    text_file.write(f"Total Votes: {len(ID)}\n")
    text_file.write("------------------------------------\n")
    for i in FinalCand:
        text_file.write(f"{analysis(i)}\n")
    text_file.write("------------------------------------\n")
    text_file.write(f"Winner: {name1[count1.index(max(count1))]}\n")
    text_file.write("------------------------------------\n")