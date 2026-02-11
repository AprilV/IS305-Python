# CHAPTER 10 - SECTION 3: CHECKING PATHS

# What: Methods to check if a path exists and what type it is
# Why: Prevent errors by checking if files/folders exist before using them
# How: Use .exists(), .is_file(), .is_dir() methods

from pathlib import Path

# Check if a path exists
win_dir = Path('C:/Windows')
print(win_dir.exists())  # True (if Windows folder exists)

# Check if it's a directory
print(win_dir.is_dir())  # True

# Check if it's a file
print(win_dir.is_file())  # False (it's a folder, not a file)

# Check a file
calc_file = Path('C:/Windows/System32/calc.exe')
print(calc_file.exists())  # True (if calc exists)
print(calc_file.is_file())  # True
print(calc_file.is_dir())  # False

# Check a non-existent path
fake_path = Path('C:/This/Does/Not/Exist')
print(fake_path.exists())  # False

# Checking for absolute vs relative paths
print(Path.cwd().is_absolute())  # True
print(Path('spam/eggs').is_absolute())  # False

# Converting relative to absolute
rel_path = Path('my/relative/path')
abs_path = rel_path.absolute()
print(abs_path)

# Or use Path.cwd()
abs_path2 = Path.cwd() / rel_path
print(abs_path2)
