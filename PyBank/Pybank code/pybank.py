# import libraries
import os
import csv

# create a path to read cvs file

#budget_data_path = os.path.join("..", "Resources", "budget_data.csv")
budget_data_path = "Resources/budget_data.csv"

#lists to store data

date = []
profit_loss = []
difference_between_profits = []

#define variables

line_count = 0
months = 0
net_profit_loss = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0
difference_between_profit = 0




# Open file

with open(budget_data_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    first_row = next(csvreader)
    Previous_profit_losses = int(first_row[1])

    #add the profit_looses_colun
    net_profit_loss += Previous_profit_losses

     # count the months
    months += 1

#for loop 
    for row in csvreader:
       
        # add months
        date.append(row[0])
       
        # count the months
        months += 1
        
        #initialize profit_losses column as an integer
        profit_losses_column = int(row[1])
        
        #add the profit_looses_colun
        net_profit_loss += profit_losses_column

     
       #calculate the difference between rows in column index 1
        difference_between_profit = profit_losses_column - Previous_profit_losses
        Previous_profit_losses = profit_losses_column

        #save the values of difference_between_profit
        difference_between_profits.append(difference_between_profit)
        
    
        # find the greatest increase
        if difference_between_profit > greatest_increase:
            greatest_increase = difference_between_profit  

        if difference_between_profit < greatest_decrease:
            greatest_decrease = difference_between_profit  

       

#calculate the changes in "profit/losses" and average
    
sum_difference_between_profit = sum(difference_between_profits)
average_in_changes = round(sum_difference_between_profit/(months - 1),2)  # substracting one from month because there is no difference within the fisrt month.

greatest_increase_month = difference_between_profits.index(greatest_increase)
greatest_decrease_month = difference_between_profits.index(greatest_decrease)
highest_month = date[greatest_increase_month]
lowest_month = date[greatest_decrease_month]
       
print("Financial Analysis")

print("________________________________________")

print(f"Total months: ${months} ")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${average_in_changes}")
print(f"Greatest Increase in Profits: {highest_month} ${greatest_increase}")
print(f"Greatest Decrease in Profits: {lowest_month} ${greatest_decrease}")

# Read in the CSV file
with open(budget_data_path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

