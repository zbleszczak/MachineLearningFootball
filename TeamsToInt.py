import pandas as pd

# Replace 'your_file.xlsx' with the path to your Excel file
file_path = 'premierleagueall.xlsx'

# Load the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Extract team names from columns 1 and 2
team_names = pd.concat([df.iloc[:, 0], df.iloc[:, 1]], ignore_index=True)

# Create a dictionary to store team names and their special numbers
team_special_numbers = {}

# Assign a unique special number to each team
for index, team in enumerate(team_names.unique()):
    team_special_numbers[team] = index + 1

# Define the output text file path
output_file_path = 'team_special_numbers.txt'

# Open the text file for writing
with open(output_file_path, 'w') as file:
    # Write the team names and their special numbers to the file
    for team, special_number in team_special_numbers.items():
        file.write(f"{team}: {special_number}\n")

print(f"Team special numbers have been saved to '{output_file_path}'")
