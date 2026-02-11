# CHAPTER 10 - SECTION 4: READING FILES

# What: Opening and reading file contents
# Why: Get data from files into your program
# How: Use open() and read() or readlines()

from pathlib import Path

# Simple method - read entire file at once
p = Path('test.txt')
# First create a test file
p.write_text('Hello, world!\nThis is line 2.\nThis is line 3.')

# Read entire file as one string
content = p.read_text()
print(content)
print(type(content))  # <class 'str'>

# Standard method - open(), read(), close()
file = open('test.txt', encoding='UTF-8')
content = file.read()
print(content)
file.close()

# Read as list of lines
file = open('test.txt', encoding='UTF-8')
lines = file.readlines()
print(lines)  # ['Hello, world!\n', 'This is line 2.\n', 'This is line 3.']
print(type(lines))  # <class 'list'>
file.close()

# Using with statement (BEST PRACTICE - auto-closes file)
with open('test.txt', encoding='UTF-8') as file:
    content = file.read()
    print(content)
# File automatically closed here!

# Read file line by line
with open('test.txt', encoding='UTF-8') as file:
    for line in file.readlines():
        print(line.strip())  # .strip() removes \n
