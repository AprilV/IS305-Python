# SECTION 1: CSV READER BASICS - Practice

# Q1: Import csv module
# WHAT IT DOES: Makes csv functions available for reading and writing CSV files
# ┌─ EXAMPLE ─────────────
# │ import sys
# └───────────────────────




# Q2: Use open() to open 'sales.csv' and store in salesFile
# WHAT IT DOES: Opens a CSV file for reading
# ┌─ EXAMPLE ─────────────
# │ myFile = open('data.csv')
# └───────────────────────




# Q3: Use csv.reader() with salesFile to create reader object and store in salesReader
# WHAT IT DOES: Creates a reader object that can iterate over CSV rows
# ┌─ EXAMPLE ─────────────
# │ reader = csv.reader(myFile)
# └───────────────────────




# Q4: Use list() to convert salesReader to list and store in salesData
# WHAT IT DOES: Converts the entire CSV into a list of lists
# ┌─ EXAMPLE ─────────────
# │ data = list(reader)
# └───────────────────────




# Q5: Print salesData
# WHAT IT DOES: Displays all the CSV data as a list
# ┌─ EXAMPLE ─────────────
# │ print(data)
# └───────────────────────




# Q6: Use salesData[1][2] to access row 1, column 2 and print it
# WHAT IT DOES: Accesses a specific cell using row and column indices
# ┌─ EXAMPLE ─────────────
# │ cell = data[0][1]
# │ print(cell)
# └───────────────────────




# Q7: Use salesFile.close() to close the file
# WHAT IT DOES: Closes the file to free resources
# ┌─ EXAMPLE ─────────────
# │ myFile.close()
# └───────────────────────




# Q8: Use open() to open 'sales.csv' again and create new csv.reader()
# WHAT IT DOES: Reopens the file for a new reader (readers can only loop once)
# ┌─ EXAMPLE ─────────────
# │ myFile = open('data.csv')
# │ reader = csv.reader(myFile)
# └───────────────────────




# Q9: Use for loop to iterate through salesReader and print line_num and row
# WHAT IT DOES: Loops through CSV rows and shows row numbers
# ┌─ EXAMPLE ─────────────
# │ for row in reader:
# │     print('Row #' + str(reader.line_num) + ' ' + str(row))
# └───────────────────────




# Q10: Use salesFile.close() to close the file
# WHAT IT DOES: Closes the file to free resources
# ┌─ EXAMPLE ─────────────
# │ myFile.close()
# └───────────────────────


