# CHAPTER 10 - SECTION 2: PATH PARTS

# What: Path objects have attributes to extract different parts of a filepath
# Why: You often need just the filename, or just the folder, or just the extension
# How: Use .name, .stem, .suffix, .parent, .parts attributes

from pathlib import Path

# Create a sample path
p = Path('C:/Users/Al/spam.txt')

# Get the filename
print(p.name)  # 'spam.txt'

# Get the filename without extension (stem)
print(p.stem)  # 'spam'

# Get the file extension
print(p.suffix)  # '.txt'

# Get the parent folder
print(p.parent)  # WindowsPath('C:/Users/Al')

# Get the anchor (root folder)
print(p.anchor)  # 'C:\\'

# Get the drive (Windows only)
print(p.drive)  # 'C:'

# Get all parts as a tuple
print(p.parts)  # ('C:\\', 'Users', 'Al', 'spam.txt')
print(p.parts[0])  # 'C:\\'
print(p.parts[-1])  # 'spam.txt'

# Access ancestor folders with parents
current = Path.cwd()
print(current.parents[0])  # One level up
print(current.parents[1])  # Two levels up
print(current.parents[2])  # Three levels up
