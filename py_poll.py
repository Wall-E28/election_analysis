import csv
import os

# # Create path to Election Results 
# file = os.path.join("Resources", "election_results.csv")

# # Open Election Results
# with open(file) as election_data:

#     # Read Election Results 
#     print(election_data)

# Create a filename variable to a direct path to a file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open file
with open(file_to_save, 'w') as election_analysis_file:

    # Write three counties to the file 
    election_analysis_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
    
