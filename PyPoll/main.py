import os
import csv


PyPoll_csv = os.path.join("resources", "election_data.csv")

total = 0
candidate_list = {}
percent_won = {}
total_won = 0
winner = ""

with open(PyPoll_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    first_row = next(csv_reader)

#total votes
    for row in csv_reader:
        total += 1

        if row[2] in candidate_list.keys():
            candidate_list[row[2]] += 1
        else:
            candidate_list[row[2]] = 1
# % of votes
    for key, value in candidate_list.items():
        percent_won[key] = round((value/total)*100,2)

    for key in candidate_list.keys():
        if candidate_list[key] > total_won:
            winner = key
            total_won = candidate_list[key]

print(f"Election Results")
print("-------------------------------------")
print("Total: " + str(total))
print("-------------------------------------")
for key, value in candidate_list.items():
    print(key + ": " + str(percent_won[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")

PyPoll_export = os.path.join("Analysis", "PyBank.text")
with open('PyBank.text', 'w+') as outfile:
    outfile.write(f"Election Results\n")
    outfile.write(f"---------------------------\n")
    outfile.write(f"Total: " + str(total) + "\n")
    outfile.write(f"---------------------------\n")
    for key, value in candidate_list.items():
        outfile.write(key + ": " + str(percent_won[key]) + "% (" + str(value) + ")\n")
    outfile.write(f"---------------------------\n")
    outfile.write(f"Winner: " + winner + "\n")
    outfile.write(f"---------------------------\n")
