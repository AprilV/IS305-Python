# CHAPTER 11 - SECTION 5: CREATING ZIP FILES

# What: Compress files into ZIP archives
# Why: Reduce file size, package multiple files for email/transfer
# How: Use zipfile module

import zipfile
from pathlib import Path

# Create a test file
with open('test.txt', 'w', encoding='utf-8') as file:
    file.write('Hello' * 1000)  # Repetitive text compresses well

# Create ZIP file and add the file
with zipfile.ZipFile('example.zip', 'w') as zip_file:
    zip_file.write('test.txt', 
                   compress_type=zipfile.ZIP_DEFLATED,
                   compresslevel=9)
print('Created example.zip')

# Add multiple files
with zipfile.ZipFile('archive.zip', 'w') as zip_file:
    zip_file.write('test.txt', compress_type=zipfile.ZIP_DEFLATED)
    # Could add more files here
    
# Append to existing ZIP (don't overwrite)
with zipfile.ZipFile('example.zip', 'a') as zip_file:
    # Create another file
    with open('another.txt', 'w', encoding='utf-8') as f:
        f.write('More content')
    zip_file.write('another.txt', compress_type=zipfile.ZIP_DEFLATED)

print('Added to existing ZIP')

# REMEMBER:
# - 'w' mode = create new (overwrites existing)
# - 'a' mode = append to existing
# - Always use compress_type=zipfile.ZIP_DEFLATED
# - compresslevel=9 is maximum compression
