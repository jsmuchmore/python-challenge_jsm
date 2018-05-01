import csv
import os

csvpath = os.path.join('resources', input("Input the file name with extension (must be in PyBank\Resources) "))


month_data = []
revenue_data = []
revenue_changes = []

with open(csvpath, newline='') as csvfile:
    csvdict = csv.DictReader(csvfile)

    for row in csvdict:
        Date = row["Date"]
        Revenue = row["Revenue"]
        
        month_data.append(row["Date"]) #create month_data list
        revenue_data.append(row["Revenue"]) #create revenue_data list

num_months = len(month_data)

total_revenue = 0

for row in  revenue_data:
    row.strip()
    total_revenue += float(row)

for i in range(1, len(revenue_data)):
    revenue_changes.append(float(revenue_data[i])-float(revenue_data[i-1]))
    max_change = max(revenue_changes)
    min_change = min(revenue_changes)


average_revenue_change = sum(revenue_changes)/len(revenue_changes)

max_change_date = ""
min_change_date = ""

for i in range(1, len(revenue_changes)):
    if revenue_changes[i] == max_change:
        max_change_date = (month_data[i+1])

for i in range(1, len(revenue_changes)):
    if revenue_changes[i] == min_change:
        min_change_date = (month_data[i+1])


#print(max_change_date)
#print(min_change_date)
#print(max_change, min_change)
#print(sum(revenue_changes))
#print(average_revenue_change)
#print(revenue_changes)

print("------------------------------")
print("Financial Analysis")
print("------------------------------")
print("Total Months: " + str(num_months))
print("Total Revenue: " + str(total_revenue))
print("Average Revenue Change: " + str(average_revenue_change))
print("Greatest Increase in Revenue: " + max_change_date + " (" + str(max_change) + ")")
print("Greatest Decrease in Revenue: " + min_change_date + " (" + str(min_change) + ")")
print("------------------------------")

with open("bank_output.txt", "w") as text_file:
    text_file.write("------------------------------\n")
    text_file.write("Financial Analysis\n")
    text_file.write("------------------------------\n")
    text_file.write("Total Months: " + str(num_months) + "\n")
    text_file.write("Total Revenue: " + str(total_revenue) + "\n")
    text_file.write("Average Revenue Change: " + str(average_revenue_change) + "\n")
    text_file.write("Greatest Increase in Revenue: " + max_change_date + " (" + str(max_change) + ")" + "\n")
    text_file.write("Greatest Decrease in Revenue: " + min_change_date + " (" + str(min_change) + ")" + "\n")
    text_file.write("------------------------------\n")








