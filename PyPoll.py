
# Add our dependencies
import csv
import os

#Assign a variable to load a ile from a path.
file_to_load= os.path.join("Resources", 'election_results.csv')

#Assign a varuable to save the file to path.
file_to_save = os.path.join('Analysis', 'election_results.txt')

# Initialize a total vote counter
total_votes= 0

# Candidate Options and candidate votes
candidate_options = []
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate= ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyse the data here.

    # Read the file object with the reader function.
    file_reader= csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)
    
    # Iterate through each row in the CSV
    for row in file_reader:
        # Add to the total vote count.
        total_votes+= 1

        #Print the candidate name from each row
        candidate_name = row[2]

        # Add the candidate name to the candidate list if not in list
        if candidate_name not in candidate_options: 
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"----------------------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"----------------------------------------\n")
        print(election_results, end="")

        # Save the final vote to the text file.
        txt_file.write(election_results)        
            
        # Determine the percentage of votes for each candidate by looping through the counts

        # Iterate through the candidate list

        for candidate_name in candidate_votes:

            # Retrive vote count of a candidate
            votes = candidate_votes[candidate_name]

            # Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100
                
            # Print the candidate name and pecentage of votes
            #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

            # Determine winning vote count and candidate
            # Determine if the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # if true, then overwrite variables
                winning_count = votes
                winning_percentage = vote_percentage
                # Set winning candidate name as candidate
                winning_candidate = candidate_name
            
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            txt_file.write(candidate_results)

        print(f"----------------------------------------\n")    
        txt_file.write(f"----------------------------------------\n")
            
        winning_candidate_summary = (
            
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"----------------------------------------\n")

        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)
            



# Print the candidate vote dictionary
# print(candidate_votes)

# Print the total votes.
#print(total_votes)

# Print the candidate list
#print(candidate_options)

#The data we need to retrieve.

# 1. The total number of votes cast
# 2. A complete list of candidates who rceived votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

