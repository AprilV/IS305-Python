# CHAPTER 12 - SECTION 3: COLORFUL TEXT WITH BEXT - Reference

# This file contains complete working examples for colorful terminal output

# IMPORTANT: Install bext first: python -m pip install bext
# NOTE: Only works when run from terminal, NOT from code editors

import bext
import time

print("=== BASIC COLOR FUNCTIONS ===")
print("(Colors only show when run from terminal)\n")

# Foreground colors
print("1. Foreground colors with bext.fg()")
colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
for color in colors:
    bext.fg(color)
    print(f"   This text is {color}")
bext.fg('reset')
print("   Back to default color\n")

# Background colors
print("2. Background colors with bext.bg()")
bext.bg('blue')
print("   This has a blue background")
bext.bg('reset')
print("   Back to default background\n")

# Combining foreground and background
print("3. Combining colors")
bext.fg('yellow')
bext.bg('blue')
print("   Yellow text on blue background")
bext.fg('reset')
bext.bg('reset')
print("   Back to normal\n")

print("=== TERMINAL INFORMATION ===")

# Terminal size
width = bext.width()
height = bext.height()
print(f"4. Terminal size: {width} columns × {height} rows")

# Terminal title
print("\n5. Setting window title")
bext.title('Python Bext Demo')
print("   Window title changed to 'Python Bext Demo'")
time.sleep(2)
bext.title('Terminal')
print("   Title reset\n")

print("=== CURSOR POSITIONING ===")

print("6. Moving cursor with bext.goto()")
print("   Watch the cursor move...\n\n\n\n")
for x in range(0, 30, 5):
    bext.goto(x, 10)
    bext.fg('green')
    print('*', end='', flush=True)
    time.sleep(0.3)

bext.goto(0, 11)
bext.fg('reset')
print("\n\n   Cursor moved across the screen!")

print("\n=== CURSOR VISIBILITY ===")

print("7. Hiding and showing cursor")
print("   Cursor will hide in 1 second...")
time.sleep(1)
bext.hide()
print("   Cursor is hidden")
time.sleep(1)
print("   Cursor will reappear in 1 second...")
time.sleep(1)
bext.show()
print("   Cursor is visible again!\n")

print("=== CLEARING SCREEN ===")

print("8. Screen will clear in 2 seconds...")
time.sleep(2)
bext.clear()
print("Screen was cleared!")
print("This is new text after clearing\n")

print("=== KEY INPUT ===")

print("9. Getting single key input with bext.get_key()")
print("   Press any key to continue...")
key = bext.get_key()
print(f"   You pressed: '{key}'\n")

print("=== ANIMATION EXAMPLE ===")

print("10. Simple animation (screen will clear)")
time.sleep(2)

for i in range(5):
    bext.clear()
    bext.goto(i * 5, 10)
    bext.fg('cyan')
    print('>>>>', end='', flush=True)
    time.sleep(0.3)

bext.clear()
bext.goto(0, 0)
bext.fg('reset')
print("Animation complete!\n")

print("=== AVAILABLE COLORS ===")
print("\nForeground and background colors:")
print("  'black', 'red', 'green', 'yellow'")
print("  'blue', 'magenta', 'purple', 'cyan', 'white'")
print("  'reset' - returns to terminal default\n")

print("=== IMPORTANT NOTES ===")
print("• Use colors sparingly - too much looks tacky")
print("• Consider accessibility - users may have color blindness")
print("• You don't know if user has light or dark terminal theme")
print("• Bext only works in terminal, not in code editors like Mu")
print("• Great for dashboards, progress indicators, and menus")
