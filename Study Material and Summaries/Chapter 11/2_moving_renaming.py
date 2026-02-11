# CHAPTER 11 - SECTION 2: MOVING AND RENAMING

# What: Move or rename files and folders
# Why: Reorganize files or rename in bulk
# How: Use shutil.move() (moving and renaming are the same operation!)

import shutil
from pathlib import Path

# Setup
h = Path.home()
(h / 'spam').mkdir(exist_ok=True)
(h / 'spam2').mkdir(exist_ok=True)
with open(h / 'spam/file1.txt', 'w', encoding='utf-8') as file:
    file.write('Hello')

# Move file to another folder (keeps name)
shutil.move(h / 'spam/file1.txt', h / 'spam2')
print('Moved file1.txt to spam2 folder')

# Create another test file
with open(h / 'spam/file2.txt', 'w', encoding='utf-8') as file:
    file.write('Hello')

# Move AND rename
shutil.move(h / 'spam/file2.txt', h / 'spam2/renamed.txt')
print('Moved and renamed to renamed.txt')

# Rename in same folder (this is just "moving" to same folder)
with open(h / 'spam/oldname.txt', 'w', encoding='utf-8') as file:
    file.write('Hello')
shutil.move(h / 'spam/oldname.txt', h / 'spam/newname.txt')
print('Renamed oldname.txt to newname.txt')

# REMEMBER:
# - Moving and renaming are the SAME operation
# - If destination is a folder: moves there, keeps name
# - If destination is a filename: moves AND renames
# - Overwrites if destination already exists!
