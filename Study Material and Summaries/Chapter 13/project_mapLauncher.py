#! python3
# mapLauncher.py - Launches a map in the browser using an address from the
# command line or clipboard.
# From: Automate the Boring Stuff with Python (3rd Edition)
# Available free at: https://automatetheboringstuff.com/
# Chapter 13 - Web Scraping

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.openstreetmap.org/search?query=' + address)
