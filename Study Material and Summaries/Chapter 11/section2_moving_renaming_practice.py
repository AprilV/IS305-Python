# SECTION 2: MOVING AND RENAMING - Practice

# Q1: Import shutil and Path from pathlib
# WHAT IT DOES: Loads modules for moving/renaming files and working with paths
# ┌─ EXAMPLE ─────────────
# │ import os
# └───────────────────────
import shutil
from pathlib import Path



# Q2: Create variable h for Path.home(), use .mkdir(exist_ok=True) to create folders h / 'Bridge_Crew' and h / 'Engineering', use with open to create file h / 'Bridge_Crew/Kirk_Orders.txt' and use f.write() to write 'Engage'
# WHAT IT DOES: Sets up folders to practice moving files between - like organizing Windows folders or Path of Exile screenshot directories
# ┌─ EXAMPLE ─────────────
# │ home = Path.home()
# │ (home / 'NFL_Stats').mkdir(exist_ok=True)
# │ (home / 'Archives').mkdir(exist_ok=True)
# │ with open(home / 'NFL_Stats/brady_touchdowns.txt', 'w', encoding='utf-8') as f:
# │     f.write('Stats data')
# └───────────────────────
h = Path.home()
(h / 'Bridge_Crew').mkdir(exist_ok=True)
(h / 'Engineering').mkdir(exist_ok=True)
# Clean up from previous runs
for f in [(h / 'Bridge_Crew/Kirk_Orders.txt'), (h / 'Engineering/Kirk_Orders.txt'), (h / 'Engineering/Red_Alert_Protocol.txt')]:
    if f.exists(): f.unlink()
with open(h / 'Bridge_Crew/Kirk_Orders.txt', 'w') as f:
    f.write('Engage')






# Q3: Using h from Q2, use shutil.move() to move h / 'Bridge_Crew/Kirk_Orders.txt' to h / 'Engineering'
# WHAT IT DOES: Transfers file from one folder to another - like moving NFL game footage from Downloads to your team's folder
# ┌─ EXAMPLE ─────────────
# │ shutil.move(h / 'NFL_Stats/brady_touchdowns.txt', h / 'Archives')
# └───────────────────────
shutil.move(h / 'Bridge_Crew/Kirk_Orders.txt', h / 'Engineering')



# Q4: Part A: Use with open to create file h / 'Bridge_Crew/Borg_Alert.txt' and use f.write() to write 'Resistance is futile'
#     Part B: Use shutil.move() to move that file to h / 'Engineering/Red_Alert_Protocol.txt' (this moves AND renames)
# WHAT IT DOES: Moves file AND renames it in one step - useful for organizing Path of Exile loot screenshots with better names
# ┌─ EXAMPLE ─────────────
# │ with open(h / 'NFL_Stats/game_notes.txt', 'w', encoding='utf-8') as f:
# │     f.write('Notes')
# │ shutil.move(h / 'NFL_Stats/game_notes.txt', h / 'Archives/playoff_strategy.txt')
# └───────────────────────
with open(h / 'Bridge_Crew/Borg_Alert.txt', 'w') as f:
    f.write('Resistance is futile')
shutil.move(h / 'Bridge_Crew/Borg_Alert.txt', h / 'Engineering/Red_Alert_Protocol.txt')




# Q5: Using h from Q2, use with open to create file h / 'Engineering/Windows95_Sounds.txt' and use f.write() to write 'Ta-da!', 
# then use shutil.move() to rename it to h / 'Engineering/XP_Startup_Sound.txt' (stays in same folder)
# WHAT IT DOES: Renames file without moving it - perfect for updating your metal band discography file names or NFL player rosters
# ┌─ EXAMPLE ─────────────
# │ with open(h / 'Archives/old_name.txt', 'w', encoding='utf-8') as f:
# │     f.write('Content')
# │ shutil.move(h / 'Archives/old_name.txt', h / 'Archives/better_name.txt')
# └───────────────────────
with open(h / 'Engineering/Windows95_Sounds.txt', 'w') as f:
    f.write('Ta-da!')
shutil.move(h / 'Engineering/Windows95_Sounds.txt', h / 'Engineering/XP_Startup_Sound.txt')
