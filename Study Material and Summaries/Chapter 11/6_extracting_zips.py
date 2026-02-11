# CHAPTER 11 - SECTION 6: READING AND EXTRACTING ZIP FILES

# What: Open ZIP files and extract contents
# Why: Access compressed data, unpack archives
# How: Use zipfile.ZipFile() to read and extract

import zipfile

# Create a test ZIP first
with zipfile.ZipFile('example.zip', 'w') as zip_file:
    with open('test.txt', 'w', encoding='utf-8') as f:
        f.write('Hello' * 1000)
    zip_file.write('test.txt', compress_type=zipfile.ZIP_DEFLATED)

# Open and read ZIP information
with zipfile.ZipFile('example.zip') as zip_file:
    # List all files in ZIP
    print(zip_file.namelist())  # ['test.txt']
    
    # Get info about a specific file
    info = zip_file.getinfo('test.txt')
    print(f'Original size: {info.file_size} bytes')
    print(f'Compressed size: {info.compress_size} bytes')
    print(f'Compression ratio: {info.file_size / info.compress_size:.2f}x')

# Extract all files
with zipfile.ZipFile('example.zip') as zip_file:
    zip_file.extractall('extracted_folder')
print('Extracted all files to extracted_folder')

# Extract single file
with zipfile.ZipFile('example.zip') as zip_file:
    zip_file.extract('test.txt', 'single_file_folder')
print('Extracted test.txt to single_file_folder')

# REMEMBER:
# - namelist() shows all files in ZIP
# - getinfo() gives file details
# - extractall() extracts everything
# - extract() extracts one file
