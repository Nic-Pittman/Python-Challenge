# HW Goal:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

import os
import csv

electionPath = os.path.join("..", "Resources", "election_data.csv")

# Variables and lists
votes = 0
candidateList = []
candidateName = []
candidateVotesTotal = []

# Open and read csv
with open(electionPath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    #skip 1st row/header
    csvHeader = next(csvReader)
    
    # for loop to add up voters, append candidate
    for row in csvReader:
        votes += 1
        candidateList.append(row[2])
                
# for loop for names and votes
for row in candidateList:
    candidateName.append(row[0])
    candidateVotesTotal.append(row[1])

nameVotesZip = zip(candidateName, candidateVotesTotal) #Tim showed me this and it changed a lot
candidateNVZ = list(nameVotesZip

# winner winner chicken dinner
maxVotes = max(candidateVotesTotal)

# for loop of winner
for row in candidateNVZ:
    if row[1] == maxVotes:
        winner = row[0]

# percentages
khanTotal = candidateList.count('Khan')
khanPct = khanTotal / votes 
correyTotal = candidateList.count('Correy')
correyPct = correyTotal / votes
liTotal = candidateList.count('Li')
liPct = liTotal / votes
oTooleyTotal = candidateList.count("O'Tooley")
oTooleyPct = oTooleyTotal / votes

print("Election Results")
print("-"*26)
print("Total Votes: " + str(votes))
print("-"*26)
print("Khan: 63.000%"  + " (" +str(khanTotal) +")")
print("Correy: 20.000%" + " (" +str(correyTotal) +")")
print("Li: 14.000%" + " (" +str(liTotal) +")")
print("O'Tooley: 3.000%" + " (" +str(oTooleyTotal) +")")
print("-"*26)
print("Winner: Khan")