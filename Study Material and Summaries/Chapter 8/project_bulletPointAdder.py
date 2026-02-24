#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
# From: Automate the Boring Stuff with Python (3rd Edition)
# Available free at: https://automatetheboringstuff.com/
# Chapter 8 - Strings and Text Editing

import pyperclip

text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):  # Loop through all indexes in the lines list
    lines[i] = '* ' + lines[i]  # Add star to each string in lines list

text = '\n'.join(lines)

pyperclip.copy(text)
