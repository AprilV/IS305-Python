"""
CSV Writer Basics - Writing CSV Files
This demonstrates writing data to CSV files
"""

import csv

# Opening file in write mode
outputFile = open('output.csv', 'w', newline='')

# Creating writer object
outputWriter = csv.writer(outputFile)

# Writing rows
outputWriter.writerow(['name', 'age', 'city'])
outputWriter.writerow(['Alice', '25', 'Seattle'])
outputWriter.writerow(['Bob', '30', 'Portland'])
outputWriter.writerow(['Charlie', '35', 'Denver'])

outputFile.close()

# Using delimiter and lineterminator
csvFile = open('custom.tsv', 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')

csvWriter.writerow(['Product', 'Price', 'Quantity'])
csvWriter.writerow(['Laptop', '999', '5'])
csvWriter.writerow(['Mouse', '25', '50'])

csvFile.close()
