# SECTION 3: DICTREADER AND DICTWRITER - Practice

# Q1: Import csv module
# WHAT IT DOES: Makes csv functions available including DictReader and DictWriter
# ┌─ EXAMPLE ─────────────
# │ import sys
# └───────────────────────




# Q2: Use open() to open 'employees.csv' and use csv.DictReader() to create empDictReader
# WHAT IT DOES: Creates a DictReader that uses first row as dictionary keys
# ┌─ EXAMPLE ─────────────
# │ myFile = open('data.csv')
# │ reader = csv.DictReader(myFile)
# └───────────────────────




# Q3: Use for loop to iterate through empDictReader and print 'Name' and 'Department' fields
# WHAT IT DOES: Loops through CSV rows as dictionaries, accessing values by column name
# ┌─ EXAMPLE ─────────────
# │ for row in reader:
# │     print(row['Title'], row['Price'])
# └───────────────────────




# Q4: Use empFile.close() to close the file
# WHAT IT DOES: Closes the file to free resources
# ┌─ EXAMPLE ─────────────
# │ myFile.close()
# └───────────────────────




# Q5: Use open() to open 'noheader.csv' and csv.DictReader() with custom headers ['id', 'item', 'cost']
# WHAT IT DOES: Creates DictReader with custom headers for CSV without header row
# ┌─ EXAMPLE ─────────────
# │ dataFile = open('values.csv')
# │ reader = csv.DictReader(dataFile, ['num', 'name', 'price'])
# └───────────────────────




# Q6: Use for loop to iterate through dataDictReader and print 'id', 'item', 'cost' fields
# WHAT IT DOES: Accesses rows using the custom headers as dictionary keys
# ┌─ EXAMPLE ─────────────
# │ for row in reader:
# │     print(row['num'], row['name'], row['price'])
# └───────────────────────




# Q7: Use dataFile.close() to close the file
# WHAT IT DOES: Closes the file to free resources
# ┌─ EXAMPLE ─────────────
# │ dataFile.close()
# └───────────────────────




# Q8: Use open() with 'w' and newline='' to open 'contacts.csv', use csv.DictWriter() with ['Name', 'Email', 'Phone']
# WHAT IT DOES: Creates DictWriter with specified column headers
# ┌─ EXAMPLE ─────────────
# │ outputFile = open('people.csv', 'w', newline='')
# │ writer = csv.DictWriter(outputFile, ['First', 'Last', 'Age'])
# └───────────────────────




# Q9: Use outputDictWriter.writeheader() to write header row
# WHAT IT DOES: Writes the column names as the first row in the CSV
# ┌─ EXAMPLE ─────────────
# │ writer.writeheader()
# └───────────────────────




# Q10: Use outputDictWriter.writerow() with {'Name': 'David', 'Email': 'd@email.com', 'Phone': '555-1111'}
# WHAT IT DOES: Writes a dictionary as a row, matching keys to columns
# ┌─ EXAMPLE ─────────────
# │ writer.writerow({'First': 'Alice', 'Last': 'Smith', 'Age': '30'})
# └───────────────────────




# Q11: Use outputDictWriter.writerow() with {'Name': 'Emma', 'Phone': '555-2222'} (missing Email)
# WHAT IT DOES: Writes row with missing values (creates empty cell for Email)
# ┌─ EXAMPLE ─────────────
# │ writer.writerow({'First': 'Bob', 'Age': '25'})
# └───────────────────────




# Q12: Use outputFile.close() to close the file
# WHAT IT DOES: Closes the file to save changes
# ┌─ EXAMPLE ─────────────
# │ outputFile.close()
# └───────────────────────


