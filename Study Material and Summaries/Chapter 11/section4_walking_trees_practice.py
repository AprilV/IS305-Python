# Chapter 11, Section 4: Walking a Directory Tree
# Based on "Automate the Boring Stuff with Python, 3rd Edition"



# QUESTION 1: Import the modules
# Import the os, shutil modules and import Path from pathlib
#┌─ EXAMPLE ─────────────
#│ import shutil
#│ from pathlib import Path
#└───────────────────────

import os, shutil
from pathlib import Path

# QUESTION 2: Use os.walk() to display the folder structure
# The os.walk() function returns three values on each iteration:
# - folder_name (string of current folder)
# - subfolders (list of subfolders in current folder)
# - filenames (list of files in current folder)
#
# Write a for loop using os.walk() that:
# - Walks through h / 'spam'
# - Prints "The current folder is " + folder_name
# - For each subfolder, prints "SUBFOLDER OF " + folder_name + ": " + subfolder
# - For each filename, prints "FILE INSIDE " + folder_name + ": " + filename
# - Prints an empty line after each folder
#┌─ EXAMPLE ─────────────
#│ h = Path.home()
#│ for folder_name, subfolders, filenames in os.walk(h / 'spam'):
#│     print('The current folder is ' + folder_name)
#│     for subfolder in subfolders:
#│         print('SUBFOLDER OF ' + folder_name + ': ' + subfolder)
#│     for filename in filenames:
#│         print('FILE INSIDE ' + folder_name + ': '+ filename)
#│     print('')
#└───────────────────────

h = Path.home()
(h / 'spam').mkdir(exist_ok=True)
(h / 'spam/eggs').mkdir(exist_ok=True)
(h / 'spam/eggs2').mkdir(exist_ok=True)
(h / 'spam/eggs/bacon').mkdir(exist_ok=True)
for f in ['spam/file1.txt', 'spam/eggs/file2.txt', 'spam/eggs/file3.txt', 'spam/eggs/bacon/file4.txt']:
    with open(h / f, 'w', encoding='utf-8') as file:
        file.write('Hello')

for folder_name, subfolders, filenames in os.walk(h / 'spam'):
    print('The current folder is ' + str(folder_name))
    
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + str(folder_name) + ': ' + subfolder)
    
    for filename in filenames:
        print('FILE INSIDE ' + str(folder_name) + ': '+ filename)
    
    print('')



# QUESTION 3: Use os.walk() to rename files to uppercase
# Modify your code from Question 2 to rename each file to uppercase.
# Inside the filenames loop, add code that:
# - Creates a Path object p from folder_name
# - Uses shutil.move(p / filename, p / filename.upper()) to rename the file
#┌─ EXAMPLE ─────────────
#│ for folder_name, subfolders, filenames in os.walk(h / 'spam'):
#│     for filename in filenames:
#│         p = Path(folder_name)
#│         shutil.move(p / filename, p / filename.upper())
#└───────────────────────

for folder_name, subfolders, filenames in os.walk(h / 'spam'):
    for filename in filenames:
        p = Path(folder_name)
        shutil.move(p / filename, p / filename.upper())

print("Section 4 complete!")

