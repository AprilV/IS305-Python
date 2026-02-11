# Chapter 11, Section 5: Creating and Adding to ZIP Files
# Based on "Automate the Boring Stuff with Python, 3rd Edition"

# ZIP files can hold compressed contents of many files. This is useful for:
# - Reducing file size for transfer over the internet
# - Packaging multiple files into one archive file
# - Creating backup systems

# QUESTION 1: Import zipfile module
#┌─ EXAMPLE ─────────────
#│ import shutil
#└───────────────────────

import zipfile

# QUESTION 2: Create a text file and compress it into a ZIP file
# Create a file named 'file1.txt' that contains the string 'Hello' repeated 10000 times.
# Then create a ZIP file named 'example.zip' in write mode ('w').
# Add file1.txt to the ZIP using compress_type=zipfile.ZIP_DEFLATED and compresslevel=9.
#
# Hint: Use with open() to create file1.txt
# Hint: Use with zipfile.ZipFile() to create example.zip
# Hint: Call the write() method on the ZipFile object
#┌─ EXAMPLE ─────────────
#│ with open('file1.txt', 'w', encoding='utf-8') as file_obj:
#│     file_obj.write('Hello' * 10000)
#│ with zipfile.ZipFile('example.zip', 'w') as example_zip:
#│     example_zip.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
#└───────────────────────

with open('file1.txt', 'w', encoding='utf-8') as file_obj:
    file_obj.write('Hello' * 10000)

with zipfile.ZipFile('example.zip', 'w') as example_zip:
    example_zip.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

# QUESTION 3: Add another file to a new ZIP archive
# Create two new files: 'file2.txt' (containing 'Data1') and 'file3.txt' (containing 'Data2').
# Create a new ZIP file named 'files.zip' in write mode.
# Add both file2.txt and file3.txt to the ZIP with compression.
#┌─ EXAMPLE ─────────────
#│ with open('file2.txt', 'w', encoding='utf-8') as file_obj:
#│     file_obj.write('Data1')
#│ with open('file3.txt', 'w', encoding='utf-8') as file_obj:
#│     file_obj.write('Data2')
#│ with zipfile.ZipFile('files.zip', 'w') as new_zip:
#│     new_zip.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)
#│     new_zip.write('file3.txt', compress_type=zipfile.ZIP_DEFLATED)
#└───────────────────────

with open('file2.txt', 'w', encoding='utf-8') as file_obj:
    file_obj.write('Data1')

with open('file3.txt', 'w', encoding='utf-8') as file_obj:
    file_obj.write('Data2')

with zipfile.ZipFile('files.zip', 'w') as new_zip:
    new_zip.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)
    new_zip.write('file3.txt', compress_type=zipfile.ZIP_DEFLATED)

# QUESTION 4: Append a file to an existing ZIP
# Create a file named 'file4.txt' containing 'Data3'.
# Open 'files.zip' in append mode ('a') - this adds to the ZIP without erasing existing files.
# Add file4.txt to the ZIP with compression.
#┌─ EXAMPLE ─────────────
#│ with open('file4.txt', 'w', encoding='utf-8') as file_obj:
#│     file_obj.write('Data3')
#│ with zipfile.ZipFile('files.zip', 'a') as new_zip:
#│     new_zip.write('file4.txt', compress_type=zipfile.ZIP_DEFLATED)
#└───────────────────────

with open('file4.txt', 'w', encoding='utf-8') as file_obj:
    file_obj.write('Data3')

with zipfile.ZipFile('files.zip', 'a') as new_zip:
    new_zip.write('file4.txt', compress_type=zipfile.ZIP_DEFLATED)

print("Section 5 complete!")

