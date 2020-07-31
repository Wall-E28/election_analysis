# Add dependencies
import csv
import os

# Create path to Election Results 
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct path to a file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Create variables for voting 
total_votes = 0
candidate_options = []

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
        
        # Add unique candidate name to candidate list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

#Print election variables
print(total_votes)
print(candidate_options)

# # Open file
# with open(file_to_save, 'w') as election_analysis_file:

#     # Write three counties to the file 
#     election_analysis_file.write("Counties in the Election\n
#     -------------------------\n
#     Arapahoe\n
#     Denver\n
#     Jefferson")
