import os
import csv

# load .csv
election_csv = os.path.join('Resources', 'election_data.csv')

# variables & lists
total_votes = 0
candidates = []
num_votes = []
percent_votes = []

# open and read csv
with open(election_csv, newline = "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csv_reader)

    for row in csv_reader:
        # count all votes
        total_votes = total_votes + 1
        # candidate name and votes
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1


    # vote percentages for each candidate
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percent_votes.append(percentage)

    # winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]



print("Election Results")
print("------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percent_votes[count]}% ({num_votes[count]})")
print("------------------------") 
print(f"Winner: {winning_candidate}")    
print("------------------------") 


with open("PyPoll_results.txt", "w") as outfile:
        outfile.write("Election Results" + "\n")
        outfile.write("------------------------" + "\n")
        outfile.write(f"Total Votes: {total_votes}" + "\n")
        outfile.write("------------------------" + "\n")
        for count in range(len(candidates)):
            outfile.write(f"{candidates[count]}: {percent_votes[count]}% ({num_votes[count]})" + "\n")
        outfile.write("------------------------" + "\n") 
        outfile.write(f"Winner: {winning_candidate}" + "\n")    
        outfile.write("------------------------" + "\n") 