# CHAPTER 11 - SECTION 4: WALKING DIRECTORY TREES

# What: Process all files in a folder and all its subfolders
# Why: Work with entire folder structures recursively
# How: Use os.walk()

import os
from pathlib import Path

# Setup - create test folder structure
h = Path.home()
(h / 'spam').mkdir(exist_ok=True)
(h / 'spam/eggs').mkdir(exist_ok=True)
(h / 'spam/eggs/bacon').mkdir(exist_ok=True)

for f in ['spam/file1.txt', 'spam/eggs/file2.txt', 'spam/eggs/bacon/file3.txt']:
    with open(h / f, 'w', encoding='utf-8') as file:
        file.write('Hello')

# Walk the directory tree
for folder_name, subfolders, filenames in os.walk(h / 'spam'):
    print(f'\nCurrent folder: {folder_name}')
    print(f'Subfolders: {subfolders}')
    print(f'Files: {filenames}')

# Process each file
for folder_name, subfolders, filenames in os.walk(h / 'spam'):
    for filename in filenames:
        print(f'Processing: {folder_name}/{filename}')

# REMEMBER:
# - os.walk() returns 3 values: folder_name, subfolders, filenames
# - Processes every folder in the tree recursively
# - Use nested loops: outer for folders, inner for files in each folder
