"""
CSV Reader Basics - Reading CSV Files
This demonstrates reading CSV files with the csv module
"""

import csv

# Opening a CSV file
exampleFile = open('data.csv')

# Creating a reader object
exampleReader = csv.reader(exampleFile)

# Converting to list of lists
exampleData = list(exampleReader)
print(exampleData)

# Accessing specific cells
print(exampleData[0][0])  # First row, first column
print(exampleData[1][2])  # Second row, third column

exampleFile.close()

# Reading with a for loop (better for large files)
exampleFile = open('data.csv')
exampleReader = csv.reader(exampleFile)

for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

exampleFile.close()
