#Import dependencies
import os
import csv



#Create variables
poll = {}
total_votes = 0
candidates = []
num_votes = []
vote_percent = []
winner_list = []

# Open and read csv file.
file = os.path.join("PyPoll","Resources", "election_data.csv")


with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread, None)


# Loops through rows, use column 3 as keys. Count votes for each candidate.
    for row in csvread:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 


for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)


# Calculate percentage of votes each candidate won.
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 1))


# Zip candidates, num_votes, vote_percent into tuples.
clean_data = list(zip(candidates, num_votes, vote_percent))


# Calculate and declare winner.
for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])
winner = winner_list[0]


# In the event of a tie, print both names. 
if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + " tied with " + winner_list[w]


# Create outputs text file
text_file = os.path.join('Output', 'election_results_' + str(file_num) +'.txt')

with open(text_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in clean_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

# Print file to terminal
with open(output_file, 'r') as readfile:
    print(readfile.read())