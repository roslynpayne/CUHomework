# PyBank
import re
import os
import csv

# set a CSV file path for the data
bank_csv = os.path.join('budget_data.csv')

# define function
def analyze_bank(data):

    # define variables
    monthsCount = 0
    netProfit = 0
    monthList = []
    monthProfit = 0
    change = 0
    changeList = []
    
    # start loop through rows
    for row in data:
       
        # add 1 to monthsCount for each row
        monthsCount += 1
        
        # increase netprofit with each row
        netProfit += int(row[1])
        
        # add each month to monthList
        monthList.append(str(row[0]))
        
        # Calculate month to month changes in profit
        # if there is previous data do the following:
        if change != 0:
            
            # set monthProfit to value in profit column
            monthProfit = int(row[1])
            
            # subtract current profit from previous month's profits to find the change
            change = monthProfit - change
            
            # change value and store it in the changeList
            changeList.append(change)
            
            # reset change variable to the value in the current profit column, next
            change = int(row[1])
            
        # if there is no previous data reset change to value in profit column (this will only apply once for the first row)
        elif change == 0:
            change = int(row[1])  
            
    # remove 1st month 
    monthList.pop(0)
    
    # find index position of the greatest increase in profits
    indxmax = changeList.index(max(changeList))

    # find index position of the greatest decrease in profits
    indxmin = changeList.index(min(changeList))

    # use index positions to find the month that corresponds with max and min values from the changeList
    maxChange = (monthList[int(indxmax)], max(changeList))
    minChange = (monthList[int(indxmin)], min(changeList))
    
    # take average of the changeList
    average = sum(changeList)/float(len(changeList))
    average = round(average,2)
    
    # print the results
    print(f'Financial Analysis')
    print(f'-------------------------------------------')
    print(f'Total Months: {monthsCount}')
    print(f'Net Profit: {netProfit}')
    print(f'Average Change: {average}')
    print(f'Greatest Increase in Profits: {maxChange}')
    print(f'Greatest Decrease In Profits: {minChange}')

    # set the file to write to
    bank_output = os.path.join("PyBankResults.txt")    
    
    # write the results to a text file
    with open(bank_output, 'w') as txtfile:
        txtfile.write('Financial Analysis')
        txtfile.write('\n------------------------------------')
        txtfile.write(f'\nTotal Months: {monthsCount}')
        txtfile.write(f'\nNet Profit: {netProfit}')
        txtfile.write(f'\nAverage Monthly Change: {average}')
        txtfile.write(f'\nGreatest Increase In Profits: {maxChange}')
        txtfile.write(f'\nGreatest Loss In Profits: {minChange}')

# read in the CSV file
with open(bank_csv, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # adjust for header
    csv_header = next(csvfile)
    
    # use function
    analyze_bank(csvreader)