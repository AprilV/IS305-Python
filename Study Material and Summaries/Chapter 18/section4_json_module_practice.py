# SECTION 4: JSON MODULE - Practice

# Q1: Import json module
# WHAT IT DOES: Makes json functions available for reading and writing JSON data
# ┌─ EXAMPLE ─────────────
# │ import sys
# └───────────────────────




# Q2: Create JSON string '{"book": "1984", "author": "Orwell", "year": 1949}' and store in jsonString
# WHAT IT DOES: Creates a string containing JSON-formatted data
# ┌─ EXAMPLE ─────────────
# │ data = '{"name": "Alice", "age": 30}'
# └───────────────────────




# Q3: Use json.loads() with jsonString to convert to Python dictionary and store in bookData
# WHAT IT DOES: Converts JSON string into Python dictionary
# ┌─ EXAMPLE ─────────────
# │ pythonDict = json.loads(data)
# └───────────────────────




# Q4: Print bookData
# WHAT IT DOES: Displays the converted dictionary
# ┌─ EXAMPLE ─────────────
# │ print(pythonDict)
# └───────────────────────




# Q5: Use bookData['book'] to access the 'book' field and print it
# WHAT IT DOES: Accesses a value from the dictionary using its key
# ┌─ EXAMPLE ─────────────
# │ print(pythonDict['name'])
# └───────────────────────




# Q6: Use bookData['year'] to access the 'year' field and print it
# WHAT IT DOES: Accesses another value from the dictionary
# ┌─ EXAMPLE ─────────────
# │ print(pythonDict['age'])
# └───────────────────────




# Q7: Create Python dictionary {'language': 'Python', 'version': 3.9, 'active': True} and store in pythonDict
# WHAT IT DOES: Creates a Python dictionary with various data types
# ┌─ EXAMPLE ─────────────
# │ myData = {'tool': 'VS Code', 'year': 2024, 'free': True}
# └───────────────────────




# Q8: Use json.dumps() with pythonDict to convert to JSON string and store in jsonOutput
# WHAT IT DOES: Converts Python dictionary into JSON-formatted string
# ┌─ EXAMPLE ─────────────
# │ jsonString = json.dumps(myData)
# └───────────────────────




# Q9: Print jsonOutput
# WHAT IT DOES: Displays the JSON string
# ┌─ EXAMPLE ─────────────
# │ print(jsonString)
# └────────────────────────────────────────────────────────┘


