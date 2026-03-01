# SECTION 2: CSV WRITER BASICS - Practice

# Q1: Import csv module
# WHAT IT DOES: Makes csv functions available for reading and writing CSV files
# ┌─ EXAMPLE ─────────────
# │ import sys
# └───────────────────────




# Q2: Use open() with 'w' mode and newline='' to open 'results.csv' and store in outputFile
# WHAT IT DOES: Opens a file for writing CSV data (newline='' prevents double-spacing on Windows)
# ┌─ EXAMPLE ─────────────
# │ myFile = open('data.csv', 'w', newline='')
# └───────────────────────




# Q3: Use csv.writer() with outputFile to create writer object and store in outputWriter
# WHAT IT DOES: Creates a writer object that can write rows to CSV file
# ┌─ EXAMPLE ─────────────
# │ writer = csv.writer(myFile)
# └───────────────────────




# Q4: Use outputWriter.writerow() to write ['title', 'year', 'rating'] as header row
# WHAT IT DOES: Writes a list as a single row in the CSV file
# ┌─ EXAMPLE ─────────────
# │ writer.writerow(['name', 'age', 'city'])
# └───────────────────────




# Q5: Use outputWriter.writerow() to write ['Inception', '2010', '8.8']
# WHAT IT DOES: Writes another row to the CSV file
# ┌─ EXAMPLE ─────────────
# │ writer.writerow(['Alice', '25', 'Seattle'])
# └───────────────────────




# Q6: Use outputWriter.writerow() to write ['Interstellar', '2014', '8.6']
# WHAT IT DOES: Writes another row to the CSV file
# ┌─ EXAMPLE ─────────────
# │ writer.writerow(['Bob', '30', 'Portland'])
# └───────────────────────




# Q7: Use outputFile.close() to close the file
# WHAT IT DOES: Closes the file to save changes
# ┌─ EXAMPLE ─────────────
# │ myFile.close()
# └───────────────────────




# Q8: Use open() with 'w' mode and newline='' to open 'custom.tsv' and store in tsvFile
# WHAT IT DOES: Opens a file for writing tab-separated data
# ┌─ EXAMPLE ─────────────
# │ dataFile = open('output.tsv', 'w', newline='')
# └───────────────────────




# Q9: Use csv.writer() with delimiter='\t' and lineterminator='\n\n' to create tsvWriter
# WHAT IT DOES: Creates writer with custom delimiter (tab) and line ending (double newline)
# ┌─ EXAMPLE ─────────────
# │ tabWriter = csv.writer(dataFile, delimiter='\t', lineterminator='\n\n')
# └───────────────────────




# Q10: Use tsvWriter.writerow() to write ['X', 'Y', 'Z'] and ['1', '2', '3']
# WHAT IT DOES: Writes rows with tab separators and double newlines
# ┌─ EXAMPLE ─────────────
# │ tabWriter.writerow(['A', 'B', 'C'])
# │ tabWriter.writerow(['4', '5', '6'])
# └───────────────────────




# Q11: Use tsvFile.close() to close the file
# WHAT IT DOES: Closes the file to save changes
# ┌─ EXAMPLE ─────────────
# │ dataFile.close()
# └───────────────────────


