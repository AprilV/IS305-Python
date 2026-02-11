# CHAPTER 12 - SECTION 2: CLIPBOARD I/O - Practice

# IMPORTANT: This section requires the pyperclip module
# RUN THIS COMMAND IN YOUR TERMINAL FIRST (not in Python):
# python -m pip install pyperclip
# On Linux: sudo apt install xclip (then install pyperclip)



# Q1: Import pyperclip module
# WHAT IT DOES: Loads the pyperclip module so you can use clipboard functions
# Example: import os
import pyperclip


# Q2: Copy Kirk's captain's log entry 'Captain's log, stardate 1701.engage!' to clipboard using pyperclip.copy()
# WHAT IT DOES: Puts text into your clipboard like you pressed Ctrl+C - useful for copying NFL stats or Path of Exile build codes to share
# Example: pyperclip.copy('Metallica - Master of Puppets')
pyperclip.copy('Hello, clipboard!')



# Q3: Get the captain's log from clipboard using pyperclip.paste() and store in variable 'enterprise_log', then print it
# WHAT IT DOES: Grabs whatever text user has copied - lets your program process NFL game stats they copied from ESPN
# Example: game_stats = pyperclip.paste()
# Example: print(game_stats)
clipboard_text = pyperclip.paste()
print(clipboard_text)





# Q4: Get Spock's message from clipboard using pyperclip.paste(), convert it to UPPERCASE using .upper() (for emergency alerts!), store in 'alert_message', copy back to clipboard using pyperclip.copy(), then print alert_message
# WHAT IT DOES: Takes clipboard text, processes it (makes uppercase like RED ALERT), puts result back - automate text transformations on copied Path of Exile item codes
# Example: metal_band = pyperclip.paste()
# Example: loud_band = metal_band.upper()
# Example: pyperclip.copy(loud_band)
# Example: print(loud_band)
text = pyperclip.paste()
uppercase_text = text.upper()
pyperclip.copy(uppercase_text)
print(uppercase_text)


# Q5: Copy a Windows 95 file path with extra spaces: 3 spaces, then 'C:\\Windows95\\Startup.wav', then 3 more spaces. Use pyperclip.copy() to copy it, pyperclip.paste() to get it back, .strip() to clean the path, store in 'clean_path', copy cleaned path back using pyperclip.copy(), then print clean_path
# WHAT IT DOES: Removes extra spaces from beginning/end - useful for cleaning up NFL player names or Path of Exile item names copied from websites
# Example: pyperclip.copy('  Brady touchdown  ')
# Example: stat = pyperclip.paste()
# Example: clean_stat = stat.strip()
# Example: pyperclip.copy(clean_stat)
# Example: print(clean_stat)
pyperclip.copy('   extra spaces   ')
data = pyperclip.paste()
cleaned = data.strip()
pyperclip.copy(cleaned)
print(cleaned)