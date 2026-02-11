# CHAPTER 10 - SECTION 5: WRITING FILES

# What: Creating and writing to files
# Why: Save data from your program to disk
# How: Use open() with 'w' (write) or 'a' (append) mode

from pathlib import Path

# Simple method - write_text()
p = Path('output.txt')
p.write_text('Hello, world!')
print(p.read_text())  # Hello, world!

# Write mode - OVERWRITES existing file
with open('output.txt', 'w', encoding='UTF-8') as file:
    file.write('First line\n')
    file.write('Second line\n')

# Append mode - ADDS to existing file
with open('output.txt', 'a', encoding='UTF-8') as file:
    file.write('Third line\n')
    file.write('Fourth line\n')

# Read the result
with open('output.txt', encoding='UTF-8') as file:
    print(file.read())

# IMPORTANT: write() does NOT add newline automatically!
with open('test.txt', 'w', encoding='UTF-8') as file:
    file.write('Line 1')  # No \n
    file.write('Line 2')  # No \n
    
with open('test.txt', encoding='UTF-8') as file:
    print(file.read())  # Line 1Line 2 (no line breaks!)

# Add \n yourself
with open('test.txt', 'w', encoding='UTF-8') as file:
    file.write('Line 1\n')
    file.write('Line 2\n')
    
with open('test.txt', encoding='UTF-8') as file:
    print(file.read())  # Now with line breaks!
