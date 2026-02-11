# CHAPTER 11 - SECTION 3: DELETING FILES (SAFELY)

# What: Delete files using send2trash (safer than permanent deletion)
# Why: Accidents happen - recycle bin lets you recover deleted files
# How: Use send2trash.send2trash() instead of os.unlink()

# NOTE: send2trash is a third-party module
# Install with: pip install send2trash

import send2trash
from pathlib import Path

# Create a test file
h = Path.home()
test_file = h / 'test_delete.txt'
with open(test_file, 'w', encoding='utf-8') as file:
    file.write('This will be deleted')

# Safe deletion - sends to recycle bin
send2trash.send2trash(str(test_file))
print('File sent to recycle bin (can be restored)')

# For comparison - PERMANENT deletion (DON'T USE unless sure!)
# import os
# os.unlink('file.txt')  # GONE FOREVER - can't restore!

# ALWAYS DO DRY RUNS before deleting!
# Comment out the deletion and use print() instead
from pathlib import Path
for filename in Path.home().glob('*.txt'):
    # send2trash.send2trash(filename)  # Commented out!
    print('Would delete:', filename)
    
# Once verified, uncomment to actually delete

# REMEMBER:
# - send2trash = safe (goes to recycle bin)
# - os.unlink = permanent (can't recover)
# - ALWAYS test with print() first!
