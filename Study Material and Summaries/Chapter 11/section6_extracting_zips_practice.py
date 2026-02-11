# Chapter 11, Section 6: Reading and Extracting from ZIP Files
# Based on "Automate the Boring Stuff with Python, 3rd Edition"

# You can read information about ZIP files and extract their contents
# using the zipfile module. This lets you examine and unpack archives.

# QUESTION 1: Import zipfile module
#┌─ EXAMPLE ─────────────
#│ import shutil
#└───────────────────────

import zipfile

# QUESTION 2: Read the contents of a ZIP file
# Open 'example.zip' (created in Section 5) and:
# - Create a ZipFile object named example_zip
# - Use the namelist() method to get a list of files in the ZIP
# - Print the list
# - Use getinfo('file1.txt') to get information about file1.txt
# - Store the result in a variable named file1_info
# - Print file1_info.file_size (original size)
# - Print file1_info.compress_size (compressed size)
# - Calculate and print how many times smaller the compressed file is
# - Close the ZipFile with example_zip.close()
#┌─ EXAMPLE ─────────────
#│ example_zip = zipfile.ZipFile('example.zip')
#│ print(example_zip.namelist())
#│ file1_info = example_zip.getinfo('file1.txt')
#│ print(file1_info.file_size)
#│ print(file1_info.compress_size)
#│ print(f'Compressed file is {round(file1_info.file_size / file1_info.compress_size, 2)}x smaller!')
#│ example_zip.close()
#└───────────────────────

example_zip = zipfile.ZipFile('example.zip')
print(example_zip.namelist())
file1_info = example_zip.getinfo('file1.txt')
print(file1_info.file_size)
print(file1_info.compress_size)
print(f'Compressed file is {round(file1_info.file_size / file1_info.compress_size, 2)}x smaller!')
example_zip.close()

# QUESTION 3: Extract all files from a ZIP
# Open 'example.zip' and extract all its contents to the current directory.
# Use the extractall() method with no arguments to extract to current directory.
# Close the ZipFile after extracting.
#┌─ EXAMPLE ─────────────
#│ example_zip = zipfile.ZipFile('example.zip')
#│ example_zip.extractall()
#│ example_zip.close()
#└───────────────────────

example_zip = zipfile.ZipFile('example.zip')
example_zip.extractall()
example_zip.close()

# QUESTION 4: Extract all files to a specific folder
# Open 'example.zip' again and extract all files into a folder named 'extracted_files'.
# The extractall() method will create the folder if it doesn't exist.
#┌─ EXAMPLE ─────────────
#│ example_zip = zipfile.ZipFile('example.zip')
#│ example_zip.extractall('extracted_files')
#│ example_zip.close()
#└───────────────────────

example_zip = zipfile.ZipFile('example.zip')
example_zip.extractall('extracted_files')
example_zip.close()

# QUESTION 5: Extract a single file from the ZIP
# Open 'example.zip' and extract only 'file1.txt' to the current directory.
# Use the extract() method with the filename as the argument.
# Then extract 'file1.txt' again, but this time to a folder named 'single_file'.
#┌─ EXAMPLE ─────────────
#│ example_zip = zipfile.ZipFile('example.zip')
#│ example_zip.extract('file1.txt')
#│ example_zip.extract('file1.txt', 'single_file')
#│ example_zip.close()
#└───────────────────────

example_zip = zipfile.ZipFile('example.zip')
example_zip.extract('file1.txt')
example_zip.extract('file1.txt', 'single_file')
example_zip.close()

print("Section 6 complete!")

