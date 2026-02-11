# CHAPTER 12 - SECTION 2: CLIPBOARD I/O - Reference

# This file contains complete working examples for clipboard operations

# IMPORTANT: Install pyperclip first: python -m pip install pyperclip
# On Linux: sudo apt install xclip

import pyperclip

print("=== BASIC CLIPBOARD OPERATIONS ===")

# Copying to clipboard
print("\n1. Copying text to clipboard")
pyperclip.copy('Hello from Python!')
print("   Copied 'Hello from Python!' to clipboard")
print("   Try pasting (Ctrl+V) in another program!")

# Reading from clipboard
print("\n2. Reading from clipboard")
content = pyperclip.paste()
print(f"   Clipboard contains: '{content}'")

print("\n=== CLIPBOARD I/O WORKFLOW ===")
print("The typical clipboard I/O program workflow:")
print("  1. Get text from clipboard with pyperclip.paste()")
print("  2. Process the text")
print("  3. Copy result back with pyperclip.copy()")

# Example: Convert clipboard text to uppercase
print("\n3. Converting clipboard text to uppercase")
original_text = pyperclip.paste()
uppercase_text = original_text.upper()
pyperclip.copy(uppercase_text)
print(f"   Original: '{original_text}'")
print(f"   Uppercase: '{uppercase_text}'")
print("   Result is now on clipboard!")

# Example: Add line numbers to clipboard text
print("\n4. Adding line numbers to clipboard text")
sample_text = """First line
Second line
Third line"""
pyperclip.copy(sample_text)
text = pyperclip.paste()
lines = text.split('\n')
numbered_lines = [f"{i+1}. {line}" for i, line in enumerate(lines)]
result = '\n'.join(numbered_lines)
pyperclip.copy(result)
print("   Original text:")
print(text)
print("\n   Numbered text (now on clipboard):")
print(result)

# Example: Strip whitespace
print("\n5. Stripping whitespace from clipboard")
messy_text = "   lots of spaces   "
pyperclip.copy(messy_text)
text = pyperclip.paste()
cleaned = text.strip()
pyperclip.copy(cleaned)
print(f"   Before: '{text}'")
print(f"   After:  '{cleaned}'")

print("\n=== REAL-WORLD USE CASES ===")
print("Clipboard I/O is great for:")
print("  • Batch processing text (format, clean, transform)")
print("  • Converting between formats (Markdown to HTML, etc.)")
print("  • Adding/removing bullets or numbering")
print("  • Case conversion")
print("  • Find and replace operations")
print("\nQuick workflow:")
print("  1. Copy input text (Ctrl+C)")
print("  2. Run your script")
print("  3. Paste result (Ctrl+V)")
