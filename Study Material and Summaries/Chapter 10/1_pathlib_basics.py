# CHAPTER 10 - SECTION 1: PATHLIB BASICS

# What: pathlib module handles file paths across different operating systems
# Why: Different OS use different path separators (\ vs /), pathlib handles this automatically
# How: Use Path() function to create path objects

from pathlib import Path

# Creating paths - Path() joins folder names with correct separator
p = Path('spam', 'bacon', 'eggs')
print(p)  # WindowsPath('spam/bacon/eggs') on Windows

# Converting to string
print(str(p))  # 'spam\\bacon\\eggs' on Windows

# Joining paths with / operator
path1 = Path('spam') / 'bacon' / 'eggs'
print(path1)  # WindowsPath('spam/bacon/eggs')

path2 = Path('spam') / Path('bacon/eggs')
print(path2)  # WindowsPath('spam/bacon/eggs')

# Getting current working directory
current = Path.cwd()
print(current)  # Shows where your program is running from

# Getting home directory
home = Path.home()
print(home)  # C:\Users\YourName on Windows

# Building paths relative to home
my_file = Path.home() / 'Documents' / 'file.txt'
print(my_file)

# REMEMBER: At least one value must be a Path object when using /
# This works: Path('spam') / 'bacon'
# This fails: 'spam' / 'bacon'  # TypeError!
