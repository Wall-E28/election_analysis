# Add dependencies
import csv
import os

# Create path to Election Results 
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct path to a file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open Election Results
with open(file_to_load, 'r') as election_data:

    # Read Election Results 
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

    # # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)

# Open file
with open(file_to_save, 'w') as election_analysis_file:

    # Write three counties to the file 
    election_analysis_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
    
