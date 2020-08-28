import os
import csv

budgetPath = os.path.join("..", "Resources", "budget_data.csv")

#HW goal: 
    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #The average of the changes in "Profit/Losses" over the entire period
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period
    
#Note to self - "#'ed out lists/variables/lines below are things I tried and kind of worked but didn't use"
    
# Set variables and lists
date = []
profitLoss = []
dateChanges = []
totalProfit = 0
totalLoss = 0
profit = 0
total = 0
months = 0
#dateList = []

# Open and read csv
with open(budgetPath) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")
    #skip 1st row/header
    csvHeader = next(csvReader)
    
    #for loop list appends and total calculation
    for row in csvReader:
        date.append(row[0])
        #dateList.append(row[0])
        months += 1
        profitLoss.append(row[1])
        profit = int(row[1])
        if profit > 0:
            totalProfit += profit
        elif profit < 0:
            totalLoss += profit
    total = totalProfit + totalLoss
    

#total number of months in the date column 
#months = len(date)

# month profitLoss value
MPL = int(profitLoss[0])

# for loop of monthly change list
for meany in range(1, len(profitLoss)):
    dateChanges.append(int(profitLoss[meany]) - MPL)
    MPL = int(profitLoss[meany])
    meany += 1
    
averageChange = sum(dateChanges) / len(dateChanges)


# greatestIncrease and greatestDecrease from dateChanges
greatestIncrease = max(dateChanges)
greatestDecrease = min(dateChanges)

#for loop to match the greatestIncrease&Decrease to their months
#for monthy in range(len(dateChanges)):
    #if dateChanges[monthy] == greatestIncrease:
        #increaseMonth = (monthy)
    #if dateChanges[monthy] == greatestDecrease:
        #decreaseMonth = (monthy)
    #else:
        #monthy += 1

#greatestIncreaseDate = dateChanges[increaseMonth]
#greatestDecreaseDate = dateChanges[decreaseMonth]
greatestIncreaseDate = date[dateChanges.index(greatestIncrease)] 
greatestDecreaseDate = date[dateChanges.index(greatestDecrease)]

print("Financial Analysis")
print("-"*66)
print("The total number of months = " + str(months))
print("The net total amount of Profit/Losses = $" +str(total))
print("The average of the changes in Profit/Losses = $" +str(averageChange))
print("The greatest increase in profits = " + str(greatestIncreaseDate) +" $ " + str(greatestIncrease))
print("The greatest decrease in losses = " + str(greatestDecreaseDate) + " $ " + str(greatestDecrease))
