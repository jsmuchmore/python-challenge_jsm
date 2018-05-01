import csv
import os

csvpath = os.path.join('resources', 'election_data_2.csv')

total_votes = 0

vote_dict ={}

with open(csvpath, newline='') as csvfile:
    csvread = csv.DictReader(csvfile, delimiter=',')

    for row in csvread:
        total_votes += 1

        if row["Candidate"] in vote_dict:
            vote_dict[row["Candidate"]] += 1
        else:
            vote_dict[row["Candidate"]] = 1

winner = max(vote_dict, key=vote_dict.get)
                

print("--------------------")
print("Election Results")
print("--------------------")
print("Total Votes: " + str(total_votes))
print("--------------------")

for k, v in vote_dict.items():
    print(k + ": "+ str((v/total_votes)*100) + "% (" + str(v) + ")")
    
print("--------------------")
print("Winner: " + winner)
print("--------------------")


with open("election_results_2.txt", "w") as text_file:
    text_file.write("------------------------------\n")
    text_file.write("Election Results\n")
    text_file.write("------------------------------\n")
    text_file.write("Total Votes: " + str(total_votes) + "\n")

    for k, v in vote_dict.items():
        text_file.write(k + ": "+ str((v/total_votes)*100) + "% (" + str(v) + ")" +"\n")

    text_file.write("------------------------------\n")
    text_file.write("Winner: " + winner + "\n")
    text_file.write("------------------------------\n")
