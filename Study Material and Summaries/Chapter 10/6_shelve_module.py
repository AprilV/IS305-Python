# CHAPTER 10 - SECTION 6: SHELVE MODULE

# What: Save Python variables to binary files
# Why: Persist data between program runs (like Save/Load features)
# How: Use shelve.open() and treat it like a dictionary

import shelve

# Save data to shelf file
shelf_file = shelve.open('mydata')
shelf_file['cats'] = ['Zophie', 'Pooka', 'Simon']
shelf_file['age'] = 25
shelf_file['colors'] = {'red': '#FF0000', 'blue': '#0000FF'}
shelf_file.close()

print('Data saved!')

# Read data from shelf file
shelf_file = shelve.open('mydata')
print(shelf_file['cats'])  # ['Zophie', 'Pooka', 'Simon']
print(shelf_file['age'])  # 25
print(shelf_file['colors'])  # {'red': '#FF0000', 'blue': '#0000FF'}
shelf_file.close()

# Get keys and values (like a dictionary)
shelf_file = shelve.open('mydata')
print(list(shelf_file.keys()))  # ['cats', 'age', 'colors']
print(list(shelf_file.values()))  # [['Zophie', 'Pooka', 'Simon'], 25, {...}]
shelf_file.close()

# Using with statement
with shelve.open('mydata') as shelf:
    shelf['new_key'] = 'new_value'
    print(shelf['new_key'])
# Auto-closed!

# REMEMBER: 
# - Shelf files work like dictionaries
# - Data is stored in binary files (not human-readable)
# - Great for saving program state, settings, etc.
