"""
DictReader and DictWriter - Working with CSV Headers
This demonstrates using headers as dictionary keys
"""

import csv

# DICTREADER - Reading with headers
exampleFile = open('dataWithHeader.csv')
exampleDictReader = csv.DictReader(exampleFile)

for row in exampleDictReader:
    print(row['Name'], row['Age'], row['City'])

exampleFile.close()

# DictReader with custom headers (no headers in file)
exampleFile = open('dataNoHeader.csv')
exampleDictReader = csv.DictReader(exampleFile, ['id', 'product', 'price'])

for row in exampleDictReader:
    print(row['id'], row['product'], row['price'])

exampleFile.close()

# DICTWRITER - Writing with headers
outputFile = open('output.csv', 'w', newline='')
outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])

# Writing header row
outputDictWriter.writeheader()

# Writing data rows
outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})
outputDictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})

outputFile.close()
