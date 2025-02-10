import pandas as pd

# Load the CSV file
df = pd.read_csv('books.csv')

# Remove duplicates based on specific columns (e.g., Mood, Interest, Book)
df_no_duplicates = df.drop_duplicates(subset=['Mood', 'Interest', 'Book'])

# Save the cleaned dataset back to CSV
df_no_duplicates.to_csv('newbooks.csv', index=False)

print("Duplicates removed and cleaned file saved as 'newbooks.csv'")
