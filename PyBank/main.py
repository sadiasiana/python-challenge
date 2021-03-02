
import os
import csv

PyBank_csv = os.path.join("resources", "budget_data.csv")


total_months = 0
net_total = 0
monthly_list = []
changes = 0
max_increase = ["", 0]
max_decrease = ["", 9999]

with open(PyBank_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    # First row
    row1 = next(csv_reader)
    total_months += 1
    net_total += int(row1[1])
    previous_net = int(row1[1])

    for row in csv_reader:
        total_months += 1
        net_total += int(row[1])
        changes = int(row[1]) - previous_net
        previous_net = int(row[1])
        monthly_list += [changes]

        if changes > max_increase[1]:
            max_increase[1] = changes
            max_increase[0] = row[0]

        if changes < max_decrease[1]:
            max_decrease[1] = changes
            max_decrease[0] = row[0]


average = sum(monthly_list) / len(monthly_list)

results = (
    f"Financial Analysis\n"
    f"---------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average}\n"
    f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})\n"
    f"Greatest Decrease in Profits: {max_decrease[0]} (${max_increase[1]})"

)

print(results)

PyBank_export = os.path.join("Analysis", "PyBank.text")
with open('PyBank.text', 'w+') as outfile:
    outfile.write(f"Financial Analysis\n")
    outfile.write(f"---------------------------\n")
    outfile.write(f"Total Months: {total_months}\n")
    outfile.write(f"Total: ${net_total}\n")
    outfile.write(f"Average Change: ${average}\n")
    outfile.write(f"Greatest Increase in Profits:, {max_increase[0]}, (${max_increase[1]})\n")
    outfile.write(f"Greatest Decrease in Profits:, {max_decrease[0]}, (${max_increase[1]})\n")
