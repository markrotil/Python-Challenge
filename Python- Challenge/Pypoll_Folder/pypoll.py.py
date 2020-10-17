# Import Dependecies
import os
import csv


vote_count = 0
voters_candidates = []

# Use import functions to call the CSV resource file
election_path = os.path.join(
    "Pypoll_Folder", "Resources", "election_data.csv")

with open(election_path, "r") as file:
    csv_read = csv.reader(file, delimiter=",")
    csv_head = next(file)

    for row in csv_read:

        vote_count += 1

        voters_candidates.append(row[2])

    Khan = int(voters_candidates.count("Khan"))
    Correy = int(voters_candidates.count("Correy"))
    Li = int(voters_candidates.count("Li"))
    OTooley = int(voters_candidates.count("O'Tooley"))

   # Get a percentage of each candidates vote total
    Khan_percentage = round((Khan/vote_count) * 100, 2)
    Correy_percentage = round((Correy/vote_count) * 100, 2)
    Li_percentage = round((Li/vote_count) * 100, 2)
    OTooley_percentage = round((OTooley/vote_count) * 100, 2)

   # Print each candidate's name, vote percentage, and raw number of votes
    #print(f"Khan: {Khan_percentage}% ({Khan})")
    #print(f"Correy: {Correy_percentage}% ({Correy})")
    #print(f"Li: {Li_percentage}% ({Li})")
    #print(f"O'Tooley: {OTooley_percentage}% ({O_Tooley})")

    # Compare Votes and pick winner with the most votes
    if Khan > Correy > Li > OTooley:
        Winner = "Khan"
    elif Correy > Khan > Li > OTooley:
        Winner = "Correy"
    elif Li > Khan > Correy > OTooley:
        Winner = "Li"
    elif OTooley > Khan > Correy > Li:
        Winner = "O'Tooley"


output = ("Election Results\n"
          "-------------------------\n"
          f"Total Votes:  {vote_count}\n"
          "-------------------------\n"
          f"Khan: {Khan_percentage}% ({Khan})\n"
          f"Correy: {Correy_percentage}% ({Correy})\n"
          f"Li: {Li_percentage}% ({Li})\n"
          f"O'Tooley: {OTooley_percentage}% ({OTooley})\n"
          "-------------------------\n"
          f"Winner: {Winner}\n"
          "-------------------------\n")


print(output)

output_path = os.path.join("analysis", "election_data.txt")
with open(output_path, 'w',) as outfile:
    outfile.write(f"{output}\n")
