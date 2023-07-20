# import libraries
import os
import csv



# create a path to read cvs file
poll_data_path = "Resources/election_data.csv"

# initialize variables
total_votes = 0
winner_vote = 0
candidate_total = 0

# Create list
candidates_names = []

#create directory to track # of votes per candidate
candidate_votes = {}

# Open file
with open(poll_data_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip the header, so it's not counted as a vote
    header = next(csvreader)

    #for loop 
    for row in csvreader:
       
        # count the months
        total_votes += 1

        #initialize candidate in column
        candidate = (row[2])

   # Add an if statement to verify if the names are in the candidates_names list.
        if candidate not in candidates_names:
            candidates_names.append(candidate)

            #track voter's count per candidate
            candidate_votes[candidate] = 0

        #Add the votes to each candidate
        candidate_votes[candidate] += 1 

    #find the max value in candidates to find the winner

    #separate the directory into 2 lists (keys and values)
        key_list = list(candidate_votes.keys())
        value_list = list(candidate_votes.values())

        winner_vote = max(value_list)
        winner_index = value_list.index(winner_vote)
        winner = key_list[winner_index]
        
    #find the percentage on each candidate
        #candidate_total = int(value_list)
        #percentage = (candidate_total / total_votes) * 100
        
  

print("Election Results")
print("_______________________________________________")

print(f"Total number of votes: {total_votes}")
for i in range(0,3):
    print(f"Candidates and individual votes: {candidates_names[i]} with {candidate_votes[candidates_names[i]]}")
print(percentage)

print(f"Winner: {winner}")


# Read in the CSV file
with open(poll_data_path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
