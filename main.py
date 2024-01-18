import csv
import os

INPUT_PATH = os.path.join("Resources", "budget_data.csv")
OUTPUT_PATH = os.path.join("analysis", "budget_analysis.txt")

month_counter = 0
total_profit = 0
change_list = []
month_list = []

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(INPUT_PATH) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        month_counter = month_counter + 1
        month_list.append(row[0])
        current_profit = int(row[1])
        total_profit = total_profit + current_profit
        if month_counter > 1:
            change = int(row[1])-previous_value
            change_list.append(change)
        previous_value = int(row[1])   

average_change = round(sum(change_list)/len(change_list),2)

max_increase = max(change_list)
max_decrease = min(change_list)

max_index = change_list.index(max_increase)
min_index = change_list.index(max_decrease)

max_increase_month = month_list[max_index + 1]
max_decrease_month = month_list[min_index + 1]

output_text = (
f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {month_counter}\n"
f"Total: ${total_profit}\n"
f"Average Change: ${average_change}\n"
f"Greatest Increase in Profits: {max_increase_month} (${max_increase})\n"
f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})"
)

print(output_text)
with open(OUTPUT_PATH,"w") as outputfile:
    outputfile.write(output_text)