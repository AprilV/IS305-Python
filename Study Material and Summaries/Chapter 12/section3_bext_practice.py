# CHAPTER 12 - SECTION 3: COLORFUL TEXT WITH BEXT - Practice

# IMPORTANT: This section requires the bext module
# RUN THIS COMMAND IN YOUR TERMINAL FIRST (not in Python):
# python -m pip install bext
# NOTE: Bext only works when run from terminal, NOT from code editors like Mu
#Done

# Q1: Import bext module
# WHAT IT DOES: Loads the bext module so you can use terminal color and formatting functions
#┌─ EXAMPLE ─────────────
#│ import sys
#└───────────────────────
import bext


# Q2: Set foreground color to 'red' (RED ALERT!) using bext.fg(), then print 'Borg shields detected!'
# WHAT IT DOES: Makes your terminal text appear in color - red for Borg alerts, green for Path of Exile loot drops
#┌─ EXAMPLE ─────────────
#│ bext.fg('blue')
#│ print('Rare item found!')
#└───────────────────────
bext.fg('red')
print('This is red text')

# Q3: Set foreground color to 'green' and background color to 'yellow' (Packers colors!) using bext.fg() and bext.bg(), then print 'Touchdown Green Bay!'
# WHAT IT DOES: Changes both text color AND background color - perfect for team colors or Windows 95 nostalgia themes
#┌─ EXAMPLE ─────────────
#│ bext.fg('white')
#│ bext.bg('black')
#│ print('Star Wars opening crawl style')
#└───────────────────────
bext.fg('green')
bext.bg('yellow')
print('Green on Yellow')


# Q4: Reset foreground and background colors using bext.fg('reset') and bext.bg('reset'), then print 'Shields back to normal'
# WHAT IT DOES: Returns colors to normal terminal defaults - use after colored alerts so your NFL stats display looks normal again
#┌─ EXAMPLE ─────────────
#│ bext.fg('reset')
#│ bext.bg('reset')
#│ print('Standard display restored')
#└───────────────────────
bext.fg('reset')
bext.bg('reset')
print('Normal colors')



# Q5: Get terminal width and height to format your Path of Exile loot table properly using bext.width() and bext.height(), store in 'screen_width' and 'screen_height', then print both
# WHAT IT DOES: Finds out how big the terminal window is - useful for formatting NFL game summaries to fit perfectly on screen
#┌─ EXAMPLE ─────────────
#│ cols = bext.width()
#│ rows = bext.height()
#│ print(f'Display: {cols}x{rows}')
#└───────────────────────
term_width = bext.width()
term_height = bext.height()
print(term_width, term_height)



# Q6: Set terminal title to 'USS Enterprise - Bridge Systems' using bext.title()
# WHAT IT DOES: Changes the text at the very top of your terminal window - make it say 'Windows 95 Simulator' or 'Path of Exile Build Calculator'
#┌─ EXAMPLE ─────────────
#│ bext.title('Brady Stats Tracker')
#└───────────────────────
bext.title('My Python Program')



# Q7: Move cursor to position x=10, y=5 (for displaying Borg approach vector coordinates) using bext.goto(), then print 'Borg cube detected at these coordinates'
# WHAT IT DOES: Positions text at specific spot on screen - useful for creating NFL scoreboard displays or Path of Exile item menus
#┌─ EXAMPLE ─────────────
#│ bext.goto(0, 0)
#│ print('Score posted at top left')
#└───────────────────────
bext.goto(10, 5)
print('Cursor moved')


# Q8: Clear the screen like a Windows 95 screen wipe using bext.clear()
# WHAT IT DOES: Erases everything on the screen - useful for starting fresh displays or clearing old Path of Exile loot lists
#┌─ EXAMPLE ─────────────
#│ bext.clear()
#└───────────────────────
