import pandas as pd

# Replace 'your_file.xlsx' with the path to your Excel file
file_path = 'Champions-League-20232024.xlsx'

# Load the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Now, you can work with the DataFrame 'df' to analyze or manipulate your match data.
print(df)