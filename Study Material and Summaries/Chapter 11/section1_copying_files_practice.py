# SECTION 1: COPYING FILES - Practice

# Q1: Import shutil and Path from pathlib
# WHAT IT DOES: Loads the modules needed to copy files and work with file paths
#┌─ EXAMPLE ─────────────
#│ import os
#└───────────────────────
import shutil 
from pathlib import Path



# Q2: Create variable h for Path.home(), use with open to create file h / 'Enterprise_Logs.txt' and use f.write() to write 'Captain Kirk - Stardate 1701'
# WHAT IT DOES: Creates a captain's log file in your home directory - like saving Windows 95 startup sounds to your retro collection
#┌─ EXAMPLE ─────────────
#│ home = Path.home()
#│ with open(home / 'game_saves.txt', 'w', encoding='utf-8') as f:
#│     f.write('Path of Exile Build')
#└───────────────────────
h = Path.home()
with open(h / 'Enterprise_Logs.txt', 'w') as f:
    f.write('Captain Kirk - Stardate 1701')
    print("Created Enterprise_Logs.txt")


# Q3: Using h from Q2, copy Enterprise_Logs.txt to h / 'Desktop' (keeps original name)
# WHAT IT DOES: Makes a backup copy of Kirk's log to Desktop - like copying NFL game highlights to your highlights folder
#┌─ EXAMPLE ─────────────
#│ shutil.copy(h / 'game_saves.txt', h / 'Documents')
#└───────────────────────
shutil.copy(h / 'Enterprise_Logs.txt', h / 'Desktop')



# Q4: Using h from Q2, copy Enterprise_Logs.txt and rename it to 'Spock_Backup.txt' in the same folder
# WHAT IT DOES: Creates a backup with a new name - like copying your Path of Exile character build and renaming it for testing
#┌─ EXAMPLE ─────────────
#│ shutil.copy(h / 'game_saves.txt', h / 'build_backup.txt')
#└───────────────────────
shutil.copy(h / 'Enterprise_Logs.txt', h / 'Spock_Backup.txt')



# Q5: Using h from Q2, create folder 'Starfleet_Archives' with a file 'Mission_Reports.txt' inside, then copy entire 
# folder to 'Starfleet_Backup'
# WHAT IT DOES: Copies entire folder with all its files - useful for backing up your Windows XP theme collections or NFL stats databases
#┌─ EXAMPLE ─────────────
#│ (h / 'Metallica_Albums').mkdir(exist_ok=True)
#│ with open(h / 'Metallica_Albums/MasterOfPuppets.txt', 'w', encoding='utf-8') as f:
#│     f.write('Album info')
#│ shutil.copytree(h / 'Metallica_Albums', h / 'Metal_Backup')
#└───────────────────────
(h / 'Starfleet_Archives').mkdir(exist_ok=True)
with open(h / 'Starfleet_Archives/Mission_Reports.txt', 'w') as f:
    f.write('Starfleet_Backup')
shutil.copytree(h / 'Starfleet_Archives', h / 'Starfleet_Backup')
