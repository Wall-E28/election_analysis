# Add dependencies
import csv
import os

# Create path to Election Results 
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct path to a file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Create variables for voting 
total_votes = 0
candidate_options = []
candidate_votes = {}

# Create variables for winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open Election Results
with open(file_to_load, 'r') as election_data:

    # Read Election Results 
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
        
        # Print candidate name from each row
        candidate_name = row[2]
        
       
        if candidate_name not in candidate_options:
            
            # Add unique candidate name to candidate list
            candidate_options.append(candidate_name)
            
            # Track votes for each candidate
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # # Print the candidate name and percentage of votes.
    # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

    # Determine Winning Candidate
    # Determine if votes is greater than winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        
        # If True, set winning count = votes, winning percentage = vote percentage,
        # and set winning candidate = candidate name
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

# Print results 
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# #Print election variables
# print(total_votes)
# print(candidate_votes)

# # Open file
# with open(file_to_save, 'w') as election_analysis_file:

#     # Write three counties to the file 
#     election_analysis_file.write("Counties in the Election\n
#     -------------------------\n
#     Arapahoe\n
#     Denver\n
#     Jefferson")
