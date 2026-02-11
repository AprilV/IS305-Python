# SECTION 3: DELETING FILES SAFELY - Practice

# FIRST: Install send2trash (run this in terminal BEFORE importing):
# C:/Users/april/AppData/Local/Python/pythoncore-3.14-64/python.exe -m pip install send2trash

# Q1: Import send2trash module and import Path from pathlib
# WHAT IT DOES: Loads module for safe deletion (sends to recycle bin instead of permanent delete)
# ┌─ EXAMPLE ─────────────
# │ import os
# └───────────────────────
import send2trash
from pathlib import Path

# Q2: Create variable h for Path.home(), use with open to create file h / 'Borg_Cube_Data.txt' and use f.write() to write '
# Tactical data', then use send2trash.send2trash(str()) to safely delete it
# WHAT IT DOES: Deletes file but sends to recycle bin - can recover if you deleted the wrong Windows theme or Path of Exile build by mistake
# ┌─ EXAMPLE ─────────────
# │ home = Path.home()
# │ with open(home / 'old_nfl_stats.txt', 'w', encoding='utf-8') as f:
# │     f.write('Last season data')
# │ send2trash.send2trash(str(home / 'old_nfl_stats.txt'))
# └───────────────────────
h =Path.home()
with open(h / 'Borg_Cube_Data.txt', 'w') as f:
    f.write('Tactical data')
send2trash.send2trash(str(h / 'Borg_Cube_Data.txt'))



# Q3: DRY RUN - use for loop with Path.home().glob('*.txt') to create variable filename, 
# print all .txt files in home directory (DON'T actually delete them)
# WHAT IT DOES: Shows what WOULD be deleted without actually deleting - always test before mass deletion of NFL stats or metal album info
# ┌─ EXAMPLE ─────────────
# │ for filename in Path.home().glob('*.log'):
# │     print('Would delete:', filename)
# └───────────────────────
for filename in Path.home().glob('*.txt'):
    print('Would delete:', filename)


# Q4: Create variable h for Path.home(), use for loop with range(3) and with open to create files h / 'Transporter_Log0.txt', h / 'Transporter_Log1.txt', h / 'Transporter_Log2.txt' and use f.write() to write 'Log entry {number}', use for loop with Path.home().glob('Transporter_Log*.txt') to print dry run, then uncomment second loop to delete all Transporter_Log files
# WHAT IT DOES: Creates test files, previews deletion, then safely removes them - like cleaning out old Windows temporary files
# ┌─ EXAMPLE ─────────────
# │ home = Path.home()
# │ for i in range(3):
# │     with open(home / f'screenshot{i}.txt', 'w', encoding='utf-8') as f:
# │         f.write(f'Game screenshot {i}')
# │ for f in Path.home().glob('screenshot*.txt'):
# │     print('Would delete:', f)
# │ # for f in Path.home().glob('screenshot*.txt'):
# └───────────────────────
h = Path.home()
for i in range(3):
    with open(h / f'Transporter_Log{i}.txt', 'w') as f:
        f.write(f'Log entry {i}')

for f in Path.home().glob('Transporter_Log*.txt'):
    print('Would delete:', f)

# Uncomment to actually delete:
# for f in Path.home().glob('Transporter_Log*.txt'):
#     send2trash.send2trash(str(f))

