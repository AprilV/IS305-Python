# CHAPTER 11 - SECTION 1: COPYING FILES

# What: Copy files and folders using shutil module
# Why: Automate backup and file organization tasks
# How: Use shutil.copy() and shutil.copytree()

import shutil
from pathlib import Path

# Setup - create test files
h = Path.home()
(h / 'spam').mkdir(exist_ok=True)
with open(h / 'spam/file1.txt', 'w', encoding='utf-8') as file:
    file.write('Hello from file1')

# Copy a single file to a folder (keeps original name)
shutil.copy(h / 'spam/file1.txt', h)
print('Copied file1.txt to home folder')

# Copy and rename
shutil.copy(h / 'spam/file1.txt', h / 'spam/file2.txt')
print('Created file2.txt as a copy')

# Copy entire folder tree
shutil.copytree(h / 'spam', h / 'spam_backup')
print('Created spam_backup folder with all contents')

# REMEMBER:
# - shutil.copy() copies ONE file
# - shutil.copytree() copies ENTIRE folder with all subfolders
# - Destination is overwritten if it already exists
