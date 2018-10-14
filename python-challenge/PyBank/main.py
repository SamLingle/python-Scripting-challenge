# Import dependencies and open file path
import os
import csv
file = os.path.join("PyBank","Resources", "budget_data.csv") 


with open(file, newline="") as csvfile:              
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    
    # Create variables to hold values.
    total_rev=0             
    prior_month_rev=0       
    total_monthly_change=0  
    max_monthly_rev_inc=0   
    max_monthly_rev_dec=0   
    
    
    # Loop throught each row/line of data in the input file (budget_csv).
    for row in csvreader:
        date = row[0]
        total_rev += float(row[1])
    # Calculate monthly revenue change. 
        # Skip first month since no previous month data.
        if csvreader.line_num == 2:
            monthly_change = 0
        else:
            monthly_change = float(row[1])-prior_month_rev
        # Add monthly_change to total.
        total_monthly_change += monthly_change  
        # While looping, find the greatest revenue increase/decrease
        if monthly_change > max_monthly_rev_inc:
            max_monthly_rev_inc = monthly_change
            date_max_rev_inc = date
        elif monthly_change < max_monthly_rev_dec:
            max_monthly_rev_dec = monthly_change
            date_max_rev_dec = date
        # Update the prior month revenue variable.
        prior_month_rev = float(row[1])
        
    #Count up total months
    total_months = int(csvreader.line_num-1) 
    
    #Print results
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    # In calculations and print statements below, various numeric values are cast to int in order to print a whole number
    print("Total Revenue: $" + str(int(total_rev))) 
    print("Average Revenue Change $" + str(int(total_monthly_change/total_months)))
    print("Greatest Increase in Revenue: " + date_max_rev_inc + " ($" +
           str(int(max_monthly_rev_inc))+")")
    print("Greatest Decrease in Revenue: " + date_max_rev_dec + " ($" +
           str(int(max_monthly_rev_dec)) + ")" )

# Export a text file with the same results.
text_file = os.path.join("instructions","PyBank",'Resources', 'Financial_Analysis_1.txt')
with open(text_file, 'w') as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write("Total Months: " + str(total_months) + "\n")
    f.write("Average Revenue Change $" + str(int(total_monthly_change/total_months)) + "\n")
    f.write("Greatest Increase in Revenue: " + date_max_rev_inc + " ($" +
           str(int(max_monthly_rev_inc)) + ")" + "\n")
    f.write("Greatest Decrease in Revenue: " + date_max_rev_dec + " ($" +
            str(int(max_monthly_rev_dec)) + ")" + "\n")