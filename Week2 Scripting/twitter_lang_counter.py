# Import pandas library for data handling
import pandas as pd

# Load tweets.csv file into a DataFrame (like a table)
df = pd.read_csv('tweets.csv')

# Create empty dictionary to store language counts
langs_count = {}

# Get just the 'lang' column from the DataFrame
col = df['lang']

# Loop through each language entry in that column
for entry in col:
    # If we've seen this language before, add 1 to its count
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # If it's a new language, add it to the dictionary with count of 1
    else:
       langs_count[entry] = 1

# Print the results (e.g., {'en': 50, 'es': 20, 'fr': 10})
print(langs_count)
