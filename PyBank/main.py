import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# lists
dates = []
profits = []
month_changes = []

# variables
count = 0 
net_profit = 0
initial_profit = 0
total_change = 0

# open and read csv
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csv_reader)
   
    # total months in dataset
    for row in csv_reader:
        count = count + 1

        # net total amount of "profit/losses"
        dates.append(row[0])
        profits.append(row[1])
        net_profit = net_profit + int(row[1])

        # average monthly change in profits
        final_profit = int(row[1])
        average_monthly_change = final_profit - initial_profit
        month_changes.append(average_monthly_change)
        total_change = total_change + average_monthly_change
        initial_profit = final_profit

        # average total change in profits
        average_total_change = (total_change/count)

        # max and min change in profits
        greatest_inc = max(month_changes)
        greatest_inc_date = dates[month_changes.index(greatest_inc)]
        
        greatest_dec = min(month_changes)
        greatest_dec_date = dates[month_changes.index(greatest_dec)]

    
    print("Financial Analysis")
    print("-------------------------------")
    print(f"Total Months: {count}")
    print(f"Total: ${net_profit}")
    print(f"Average Change: ${int(average_total_change)}")
    print(f"Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc})")
    print(f"Greatest Decrease in Profits: {greatest_dec_date} (${greatest_dec})")

    with open("PyBank_results.txt", "w") as outfile:
        outfile.write("Financial Analysis" + "\n")
        outfile.write("-------------------------------" + "\n")
        outfile.write(f"Total Months: {count}" + "\n")
        outfile.write(f"Total: ${net_profit}" + "\n")
        outfile.write(f"Average Change: ${int(average_total_change)}" + "\n")
        outfile.write(f"Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc})" + "\n")
        outfile.write(f"Greatest Decrease in Profits: {greatest_dec_date} (${greatest_dec})" + "\n")



