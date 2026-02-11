===============================================================================
IS 305 - CHAPTER 11: ORGANIZING FILES - COMPLETE STUDY GUIDE
Automate the Boring Stuff with Python, 3rd Edition
===============================================================================

COURSE INFORMATION:
- Class: IS 305 (Information Systems)
- Final Year Bachelor's Degree (Second to Last Term)
- Textbook: Automate the Boring Stuff with Python, 3rd Edition
- Purpose: Study guide and command reference for final project
- Date: February 6, 2026

===============================================================================
CHAPTER OVERVIEW
===============================================================================

Chapter 11 focuses on automating file organization tasks:
- Copying, moving, and renaming files with shutil module
- Safely deleting files to recycle bin with send2trash
- Walking directory trees with os.walk()
- Compressing and extracting ZIP files
- Creating automated file organization projects

WHY THIS MATTERS:
Manual file organization (copying hundreds of files, renaming sequences, 
creating backups) can take hours or days. Python can automate these boring 
tasks in seconds, handling:
- Bulk copying PDFs from multiple folders
- Renaming hundreds of files systematically
- Creating incremental backups as ZIP archives
- Organizing files by type, date, or other criteria
- Safely managing large file operations

This chapter transforms your computer into a tireless file clerk that never 
makes mistakes.

===============================================================================
THE shutil MODULE - FILE OPERATIONS
===============================================================================

WHAT IS shutil?
Short for "shell utilities" - provides functions to copy, move, rename, and 
delete files and folders.

IMPORTING:

>>> import shutil

All shutil functions accept either strings or Path objects as arguments.

SETUP FOR EXAMPLES:

Create test files and folders:
>>> from pathlib import Path
>>> h = Path.home()
>>> (h / 'spam').mkdir(exist_ok=True)
>>> with open(h / 'spam/file1.txt', 'w', encoding='utf-8') as file:
...     file.write('Hello')

This creates:
- A folder named 'spam' in your home directory
- A text file 'file1.txt' inside it

===============================================================================
COPYING FILES
===============================================================================

FUNCTION: shutil.copy(source, destination)

WHAT IT DOES:
Copies the file at source path to the destination

RETURNS:
The path of the copied file (as a string)

TWO BEHAVIORS:

Behavior 1: Destination is a folder
Copies file with its original name to that folder

Behavior 2: Destination is a filename
Copies file AND renames it

EXAMPLES:

Example 1: Copy to folder (keeps original name)
>>> import shutil
>>> from pathlib import Path
>>> h = Path.home()
>>> shutil.copy(h / 'spam/file1.txt', h)
'C:\\Users\\Al\\file1.txt'

WHAT HAPPENED:
- Source: C:\Users\Al\spam\file1.txt
- Destination: C:\Users\Al (home folder)
- Result: C:\Users\Al\file1.txt (same name, new location)

Example 2: Copy and rename
>>> shutil.copy(h / 'spam/file1.txt', h / 'spam/file2.txt')
WindowsPath('C:/Users/Al/spam/file2.txt')

WHAT HAPPENED:
- Source: C:\Users\Al\spam\file1.txt
- Destination: C:\Users\Al\spam\file2.txt (new filename)
- Result: Created file2.txt (copy with new name in same folder)

IMPORTANT NOTES:
- If destination file already exists, it will be overwritten
- Only copies the file, not its metadata (permissions, timestamps)
- Does NOT copy folders - only individual files

===============================================================================
COPYING FOLDERS
===============================================================================

FUNCTION: shutil.copytree(source, destination)

WHAT IT DOES:
Copies entire folder, including all files and subfolders

RETURNS:
The path of the copied folder

EXAMPLE:

>>> import shutil
>>> from pathlib import Path
>>> h = Path.home()
>>> shutil.copytree(h / 'spam', h / 'spam_backup')
WindowsPath('C:/Users/Al/spam_backup')

WHAT HAPPENED:
Created spam_backup folder with exact copy of spam folder's contents:

Before:
C:\Users\Al\
└── spam\
    └── file1.txt

After:
C:\Users\Al\
├── spam\
│   └── file1.txt
└── spam_backup\
    └── file1.txt

USE CASE:
Perfect for creating backups of entire project folders!

IMPORTANT NOTES:
- Copies everything recursively (all subfolders and files)
- Destination folder must NOT already exist (will raise error)
- Great for backing up before making major changes

===============================================================================
MOVING AND RENAMING FILES AND FOLDERS
===============================================================================

FUNCTION: shutil.move(source, destination)

WHAT IT DOES:
Moves file or folder from source to destination

RETURNS:
String of the new absolute path

KEY CONCEPT:
Moving and renaming are the SAME operation - just changing the path!

BEHAVIOR 1: Destination is an existing folder
Moves source into that folder, keeps original name

EXAMPLE:

>>> import shutil
>>> from pathlib import Path
>>> h = Path.home()
>>> (h / 'spam2').mkdir()
>>> shutil.move(h / 'spam/file1.txt', h / 'spam2')
'C:\\Users\\Al\\spam2\\file1.txt'

WHAT HAPPENED:
- Created spam2 folder
- Moved file1.txt from spam folder to spam2 folder
- File no longer exists in spam folder
- If file1.txt already existed in spam2, it would be overwritten

Before:
spam\
└── file1.txt
spam2\
(empty)

After:
spam\
(empty)
spam2\
└── file1.txt

BEHAVIOR 2: Destination is not an existing folder
Moves AND renames the file

EXAMPLE:

>>> shutil.move(h / 'spam/file1.txt', h / 'spam2/new_name.txt')
'C:\\Users\\Al\\spam2\\new_name.txt'

WHAT HAPPENED:
- Moved file from spam folder to spam2 folder
- Renamed it from file1.txt to new_name.txt
- All in one operation!

RENAMING IN SAME FOLDER:

>>> shutil.move(h / 'spam/oldname.txt', h / 'spam/newname.txt')

This "moves" the file to the same folder but with a new name = RENAME!

IMPORTANT NOTES:
- Source file/folder is REMOVED from original location
- Overwrites destination if it already exists
- Works for both files and folders
- Can move across different drives/partitions

===============================================================================
PERMANENTLY DELETING FILES AND FOLDERS
===============================================================================

THREE DELETION FUNCTIONS:

1. shutil.rmtree(path) - Delete folder and ALL contents
2. os.unlink(path) - Delete single file
3. os.rmdir(path) - Delete single EMPTY folder

WARNING: These deletions are PERMANENT - files don't go to recycle bin!

FUNCTION 1: shutil.rmtree(path)

>>> import shutil
>>> shutil.rmtree('C:\\folder_to_delete')

WHAT IT DOES:
- Deletes the entire folder tree
- Removes all files inside
- Removes all subfolders inside
- Everything GONE permanently!

USE WITH EXTREME CAUTION!

FUNCTION 2: os.unlink(path)

>>> import os
>>> os.unlink('C:\\file.txt')

WHAT IT DOES:
- Deletes a single file
- File must exist (error if not)
- Permanent deletion

FUNCTION 3: os.rmdir(path)

>>> import os
>>> os.rmdir('C:\\empty_folder')

WHAT IT DOES:
- Deletes a single folder
- Folder MUST be empty (error if not)
- Permanent deletion

===============================================================================
SAFE PRACTICES - DRY RUNS
===============================================================================

CONCEPT: Test your code BEFORE actually deleting files

THE PROBLEM:

This code has a typo (looks for .rxt instead of .txt):
```python
import os
from pathlib import Path
for filename in Path.home().glob('*.rxt'):
    os.unlink(filename)
```

If you run this, it might delete important .rxt files by mistake!

THE SOLUTION - DRY RUN:

Comment out the deletion and add print() instead:
```python
import os
from pathlib import Path
for filename in Path.home().glob('*.rxt'):
    #os.unlink(filename)  # Commented out!
    print('Would delete:', filename)
```

WHAT THIS DOES:
- Shows you EXACTLY what would be deleted
- Doesn't actually delete anything
- Lets you verify the code is correct

WORKFLOW:

1. Write code with deletion commands commented out
2. Add print() statements to show what would happen
3. Run the program and verify output
4. If correct, uncomment deletion code and run for real
5. If wrong, fix the code and repeat

ADDITIONAL SAFETY MEASURES:
- Create backup copies before running deletion scripts
- Test on a small subset of files first
- Use version control (Git) for important projects
- Double-check glob patterns before running

REMEMBER: You can't undo permanent deletions!

===============================================================================
DELETING TO RECYCLE BIN - send2trash MODULE
===============================================================================

THE PROBLEM WITH PERMANENT DELETION:
shutil.rmtree() and os.unlink() delete files FOREVER - no getting them back!

THE SOLUTION: send2trash module

WHAT IT DOES:
Sends files to recycle bin (Windows) or trash (macOS/Linux) instead of 
permanently deleting them. You can restore files if needed!

INSTALLATION:

send2trash is a third-party module (not built into Python). Install it:
```
pip install send2trash
```

USAGE:

>>> import send2trash
>>> send2trash.send2trash('file1.txt')

WHAT HAPPENED:
- file1.txt moved to recycle bin
- Can be restored if needed
- Doesn't free disk space until you empty recycle bin

COMPARISON:

Permanent deletion (os.unlink):
>>> os.unlink('file.txt')
# File is GONE forever!

Safe deletion (send2trash):
>>> send2trash.send2trash('file.txt')
# File in recycle bin - can restore it!

WHEN TO USE EACH:

Use send2trash when:
- Testing new scripts
- Working with important files
- You might need to undo deletions
- Safety is more important than disk space

Use os.unlink/rmtree when:
- Absolutely sure files should be deleted
- Need to free disk space immediately
- Working with temporary files
- Automating routine cleanup

IMPORTANT LIMITATIONS:
- send2trash can only DELETE files, not restore them
- To restore, use your OS's recycle bin interface
- Recycle bin has size limits (old files auto-deleted)

BEST PRACTICE:
Default to send2trash unless you specifically need permanent deletion.

===============================================================================
WALKING A DIRECTORY TREE
===============================================================================

THE PROBLEM:
You need to process files in a folder AND all its subfolders, and all their 
subfolders, and so on...

THE SOLUTION: os.walk()

WHAT IT DOES:
Walks through every folder in a directory tree, giving you access to all 
files and subfolders at each level

SETUP - CREATE TEST FOLDER STRUCTURE:

>>> from pathlib import Path
>>> h = Path.home()
>>> (h / 'spam').mkdir(exist_ok=True)
>>> (h / 'spam/eggs').mkdir(exist_ok=True)
>>> (h / 'spam/eggs2').mkdir(exist_ok=True)
>>> (h / 'spam/eggs/bacon').mkdir(exist_ok=True)
>>> for f in ['spam/file1.txt', 'spam/eggs/file2.txt', 
...          'spam/eggs/file3.txt', 'spam/eggs/bacon/file4.txt']:
...     with open(h / f, 'w', encoding='utf-8') as file:
...         file.write('Hello')

RESULTING STRUCTURE:

spam\
├── file1.txt
├── eggs\
│   ├── file2.txt
│   ├── file3.txt
│   └── bacon\
│       └── file4.txt
└── eggs2\
    (empty)

BASIC os.walk() USAGE:

>>> import os
>>> from pathlib import Path
>>> h = Path.home()
>>> for folder_name, subfolders, filenames in os.walk(h / 'spam'):
...     print(f'Current folder: {folder_name}')
...     print(f'Subfolders: {subfolders}')
...     print(f'Files: {filenames}')
...     print()

OUTPUT:

Current folder: C:\Users\Al\spam
Subfolders: ['eggs', 'eggs2']
Files: ['file1.txt']

Current folder: C:\Users\Al\spam\eggs
Subfolders: ['bacon']
Files: ['file2.txt', 'file3.txt']

Current folder: C:\Users\Al\spam\eggs\bacon
Subfolders: []
Files: ['file4.txt']

Current folder: C:\Users\Al\spam\eggs2
Subfolders: []
Files: []

HOW IT WORKS:

os.walk() returns three values on each iteration:

1. folder_name (string): Current folder's path
2. subfolders (list): Names of subfolders in current folder
3. filenames (list): Names of files in current folder

PRACTICAL EXAMPLE - RENAME ALL FILES TO UPPERCASE:

```python
import os, shutil
from pathlib import Path
h = Path.home()

for folder_name, subfolders, filenames in os.walk(h / 'spam'):
    folder_name = Path(folder_name)
    print(f'Adding files in folder {folder_name}...')
    
    for filename in filenames:
        print(f'Renaming file {filename}...')
        # Rename file to uppercase:
        shutil.move(folder_name / filename, 
                   folder_name / filename.upper())
```

WHAT THIS DOES:
- Walks through spam folder and all subfolders
- For each file found, renames it to UPPERCASE
- file1.txt → FILE1.TXT
- file2.txt → FILE2.TXT
- And so on...

NESTED LOOPS STRUCTURE:

```python
for folder_name, subfolders, filenames in os.walk(path):
    # Outer loop: once per folder
    
    for subfolder in subfolders:
        # Inner loop 1: process each subfolder
        pass
    
    for filename in filenames:
        # Inner loop 2: process each file
        pass
```

IMPORTANT NOTES:
- os.walk() doesn't change the current working directory
- You can modify files while walking (rename, move, delete)
- Processing happens top-down by default (parents before children)
- Returns lists of names, not full paths (combine with folder_name)

USE CASES:
- Find all files of a certain type across entire project
- Back up all files recursively
- Rename files in bulk across many folders
- Calculate total size of all files
- Search for specific content in any file

===============================================================================
COMPRESSING FILES - zipfile MODULE
===============================================================================

WHAT ARE ZIP FILES?
- Archive files with .zip extension
- Contain compressed contents of multiple files/folders
- Reduce file size for faster transfer
- Package many files into one convenient file

WHY USE ZIP FILES?
- Email attachments (easier to send one file than many)
- Reduce bandwidth when uploading/downloading
- Organize related files together
- Create simple backups

===============================================================================
CREATING ZIP FILES
===============================================================================

BASIC PROCESS:

1. Open ZIP file in write mode
2. Add files to it
3. Close the ZIP file

EXAMPLE:

>>> import zipfile

# Create a test file
>>> with open('file1.txt', 'w', encoding='utf-8') as file_obj:
...     file_obj.write('Hello' * 10000)

# Create ZIP file and add the test file
>>> with zipfile.ZipFile('example.zip', 'w') as example_zip:
...     example_zip.write('file1.txt', 
...                      compress_type=zipfile.ZIP_DEFLATED,
...                      compresslevel=9)

WHAT HAPPENED:
- Created file1.txt with 50,000 characters (~49KB)
- Created example.zip
- Compressed file1.txt into the ZIP (~213 bytes!)
- That's 99.5% compression for repetitive data!

BREAKING DOWN THE CODE:

zipfile.ZipFile('example.zip', 'w')
- First argument: ZIP filename to create
- Second argument: 'w' for write mode
- Opens ZIP file for writing

example_zip.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED, 
                 compresslevel=9)
- First argument: File to add to ZIP
- compress_type=zipfile.ZIP_DEFLATED: Use deflate compression algorithm
- compresslevel=9: Maximum compression (0-9 scale, 9=most compressed/slowest)

ZIP FILE MODES:

'w' = Write mode (creates new ZIP or overwrites existing)
'a' = Append mode (adds to existing ZIP without erasing)

IMPORTANT NOTES:
- Write mode ERASES existing ZIP file completely
- Use append mode to add files to existing ZIP
- Always specify compress_type for actual compression
- Without compression, files are just stored (no size reduction)
- compresslevel added in Python 3.7+ (default is 6)

ADDING MULTIPLE FILES:

>>> with zipfile.ZipFile('archive.zip', 'w') as zip_file:
...     zip_file.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED)
...     zip_file.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)
...     zip_file.write('file3.txt', compress_type=zipfile.ZIP_DEFLATED)

APPENDING TO EXISTING ZIP:

>>> with zipfile.ZipFile('example.zip', 'a') as example_zip:
...     example_zip.write('another_file.txt', 
...                      compress_type=zipfile.ZIP_DEFLATED)

===============================================================================
READING ZIP FILES
===============================================================================

GETTING ZIP FILE INFORMATION:

>>> import zipfile
>>> example_zip = zipfile.ZipFile('example.zip')
>>> example_zip.namelist()
['file1.txt']

namelist() returns list of all files in the ZIP

GETTING DETAILED FILE INFO:

>>> file1_info = example_zip.getinfo('file1.txt')
>>> file1_info.file_size
50000
>>> file1_info.compress_size
97
>>> f'Compressed file is {round(file1_info.file_size / file1_info.compress_size, 2)}x smaller!'
'Compressed file is 515.46x smaller!'
>>> example_zip.close()

WHAT THESE ATTRIBUTES MEAN:

file_size: Original uncompressed size in bytes
compress_size: Compressed size in bytes

OBJECTS INVOLVED:

ZipFile object: Represents the entire ZIP archive
ZipInfo object: Information about ONE file in the archive

THE FLOW:

1. Create ZipFile object for the ZIP archive
2. Call getinfo() to get ZipInfo object for specific file
3. Access ZipInfo attributes for file details

COMPRESSION RATIO CALCULATION:

original_size / compressed_size = compression ratio
50000 / 97 = 515.46x smaller

This shows how effective compression is!

IMPORTANT: Always close() the ZipFile when done, or use with statement

===============================================================================
EXTRACTING FROM ZIP FILES
===============================================================================

METHOD 1: extractall() - Extract everything

>>> import zipfile
>>> example_zip = zipfile.ZipFile('example.zip')
>>> example_zip.extractall()
>>> example_zip.close()

WHAT IT DOES:
- Extracts ALL files and folders from ZIP
- Puts them in current working directory
- Creates subfolders as needed

EXTRACTING TO SPECIFIC FOLDER:

>>> example_zip.extractall('C:\\spam')

- Extracts to C:\spam folder
- Creates C:\spam if it doesn't exist

METHOD 2: extract() - Extract single file

>>> example_zip = zipfile.ZipFile('example.zip')
>>> example_zip.extract('file1.txt')
'C:\\Users\\Al\\Desktop\\file1.txt'

RETURNS: Path where file was extracted

EXTRACTING SINGLE FILE TO SPECIFIC FOLDER:

>>> example_zip.extract('file1.txt', 'C:\\some\\new\\folders')
'C:\\some\\new\\folders\\file1.txt'

WHAT IT DOES:
- Extracts only file1.txt
- Creates C:\some\new\folders if needed
- Returns the full path of extracted file

IMPORTANT NOTES:
- File names must match exactly (from namelist())
- Folders created automatically if needed
- Existing files will be overwritten
- Always close ZIP file when done

USING WITH STATEMENTS (SAFER):

>>> with zipfile.ZipFile('example.zip') as zip_file:
...     zip_file.extractall('output_folder')
# Automatically closed!

===============================================================================
PROJECT: BACKUP TO ZIP
===============================================================================

PROBLEM:
You're working on a project in C:\Users\Al\AlsPythonBook and want to create 
incremental backup ZIP files like:
- AlsPythonBook_1.zip
- AlsPythonBook_2.zip
- AlsPythonBook_3.zip
And so on...

Doing this manually is tedious and error-prone!

SOLUTION:
Automate it with Python!

THE PROGRAM WILL:
1. Figure out the next available number
2. Create a ZIP file with that number
3. Walk through the folder tree
4. Add all files to the ZIP

STEP 1: DETERMINE ZIP FILENAME

```python
import zipfile, os
from pathlib import Path

def backup_to_zip(folder):
    folder = Path(folder)  # Ensure it's a Path object
    
    # Find the next available number
    number = 1
    while True:
        zip_filename = Path(folder.parts[-1] + '_' + str(number) + '.zip')
        if not zip_filename.exists():
            break
        number = number + 1
```

HOW IT WORKS:

folder.parts[-1]:
If folder is C:\Users\Al\spam, parts[-1] is 'spam'

Loop logic:
- Start with number = 1
- Check if spam_1.zip exists
- If exists, increment number and check spam_2.zip
- Keep going until finding non-existent file
- That's the filename we'll use!

STEP 2: CREATE THE ZIP FILE

```python
    print(f'Creating {zip_filename}...')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')
```

Opens ZIP file in write mode

STEP 3: WALK DIRECTORY AND ADD FILES

```python
    # Walk the entire folder tree
    for folder_name, subfolders, filenames in os.walk(folder):
        folder_name = Path(folder_name)
        print(f'Adding files in folder {folder_name}...')
        
        # Add all files in this folder
        for filename in filenames:
            print(f'Adding file {filename}...')
            backup_zip.write(folder_name / filename)
    
    backup_zip.close()
    print('Done.')
```

WHAT THIS DOES:
- Walks through folder and all subfolders
- Prints progress messages
- Adds each file to the ZIP
- Closes ZIP when complete

COMPLETE PROGRAM:

```python
# backup_to_zip.py
import zipfile, os
from pathlib import Path

def backup_to_zip(folder):
    folder = Path(folder)
    
    # Figure out the ZIP filename
    number = 1
    while True:
        zip_filename = Path(folder.parts[-1] + '_' + str(number) + '.zip')
        if not zip_filename.exists():
            break
        number = number + 1
    
    # Create the ZIP file
    print(f'Creating {zip_filename}...')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')
    
    # Walk and compress
    for folder_name, subfolders, filenames in os.walk(folder):
        folder_name = Path(folder_name)
        print(f'Adding files in folder {folder_name}...')
        
        for filename in filenames:
            print(f'Adding file {filename}...')
            backup_zip.write(folder_name / filename)
    
    backup_zip.close()
    print('Done.')

# Run the backup
backup_to_zip(Path.home() / 'spam')
```

EXAMPLE OUTPUT:

```
Creating spam_1.zip...
Adding files in C:\Users\Al\spam...
Adding file file1.txt...
Adding files in C:\Users\Al\spam\eggs...
Adding file file2.txt...
Done.
```

RUN IT AGAIN:

```
Creating spam_2.zip...
Adding files in C:\Users\Al\spam...
Adding file file1.txt...
Done.
```

Notice it created spam_2.zip automatically!

EXTENSIONS YOU COULD ADD:
- Only backup files with certain extensions (.py, .txt)
- Exclude certain file types (.exe, .tmp)
- Add timestamp to filename instead of number
- Compress only files modified since last backup
- Add compression settings for better size reduction

THE POWER OF AUTOMATION:
- Manual backup: Minutes of repetitive work
- Python script: Seconds, always accurate, never forgets!

===============================================================================
CHAPTER SUMMARY
===============================================================================

KEY CONCEPTS LEARNED:

1. SHUTIL MODULE - FILE OPERATIONS
   - shutil.copy(source, dest): Copy single file
   - shutil.copytree(source, dest): Copy entire folder tree
   - shutil.move(source, dest): Move or rename file/folder
   - All accept Path objects or strings

2. DELETING FILES
   - shutil.rmtree(path): Delete folder and all contents
   - os.unlink(path): Delete single file
   - os.rmdir(path): Delete empty folder
   - send2trash.send2trash(path): Safe deletion to recycle bin

3. SAFE PRACTICES
   - Always do dry runs before deleting
   - Comment out destructive operations, add print() instead
   - Create backups before running file scripts
   - Use send2trash instead of permanent deletion when testing

4. WALKING DIRECTORY TREES
   - os.walk(path) visits every folder in a tree
   - Returns (folder_name, subfolders, filenames) on each iteration
   - Perfect for processing all files recursively
   - Doesn't change working directory

5. ZIP FILES
   - zipfile.ZipFile(name, mode): Open ZIP archive
   - write(): Add files with compression
   - namelist(): List all files in ZIP
   - extractall(): Extract everything
   - extract(): Extract single file
   - Use with statements for automatic cleanup

6. AUTOMATION BENEFITS
   - Process thousands of files in seconds
   - Never make numbering mistakes
   - Create consistent backups
   - Organize files by any criteria
   - Free up hours of manual work

7. REAL-WORLD APPLICATIONS
   - Automated backups
   - Bulk file renaming
   - Organizing downloads by file type
   - Creating archive snapshots
   - Cleaning up old files

===============================================================================
PRACTICE QUESTIONS WITH DETAILED ANSWERS
===============================================================================

1. What is the difference between shutil.copy() and shutil.copytree()?

ANSWER:
- shutil.copy() copies a single file
- shutil.copytree() copies an entire folder and all its contents

DETAILED EXPLANATION:

shutil.copy():
- Copies ONE file from source to destination
- Does NOT copy folders
- Destination can be a folder (keeps name) or filename (renames)
- Example: shutil.copy('file.txt', 'backup/')

shutil.copytree():
- Copies entire folder tree recursively
- Includes all files, subfolders, and their contents
- Destination folder must NOT already exist
- Example: shutil.copytree('project/', 'project_backup/')

Use shutil.copy() for single files, shutil.copytree() for whole folders.

---

2. What function is used to rename files?

ANSWER: shutil.move()

DETAILED EXPLANATION:

The shutil.move() function is used to rename files because renaming IS 
moving - you're just moving to the same folder with a different name.

Example - Renaming in same folder:
>>> shutil.move('old_name.txt', 'new_name.txt')

This "moves" the file to the same location but with a new name.

Example - Moving AND renaming:
>>> shutil.move('folder1/old_name.txt', 'folder2/new_name.txt')

This moves the file to a different folder AND gives it a new name.

There's no separate "rename" function - shutil.move() handles both 
moving and renaming in one operation.

---

3. What is the difference between the delete functions in the send2trash 
and shutil modules?

ANSWER:
- send2trash: Moves files to recycle bin (can restore)
- shutil.rmtree(): Permanently deletes (cannot restore)

DETAILED EXPLANATION:

send2trash.send2trash():
- Sends files to recycle bin / trash
- Files can be restored if needed
- Safer for testing and important files
- Doesn't free disk space until bin is emptied
- Requires third-party module installation

shutil.rmtree() (and os.unlink()):
- Permanently deletes files immediately
- Cannot be undone or restored
- Frees disk space right away
- Built into Python (no installation needed)
- Dangerous if used incorrectly

BEST PRACTICE:
Use send2trash during development and testing.
Use shutil/os functions only when permanent deletion is certain.

Example comparison:
>>> send2trash.send2trash('file.txt')  # Safe - can restore
>>> os.unlink('file.txt')  # GONE FOREVER

---

4. ZipFile objects have a close() method just like File objects' close() 
method. What ZipFile method is equivalent to File objects' open() method?

ANSWER: zipfile.ZipFile()

DETAILED EXPLANATION:

For regular files:
- open() creates a File object
- close() closes the File object

For ZIP files:
- zipfile.ZipFile() creates a ZipFile object (equivalent to open())
- close() closes the ZipFile object (same as files)

Example comparison:

Regular file:
>>> file = open('data.txt', 'w', encoding='UTF-8')  # open()
>>> file.write('Hello')
>>> file.close()  # close()

ZIP file:
>>> zip_file = zipfile.ZipFile('archive.zip', 'w')  # ZipFile() = open()
>>> zip_file.write('file.txt')
>>> zip_file.close()  # close()

Both use with statements for automatic closing:

Regular file:
>>> with open('data.txt', 'w', encoding='UTF-8') as f:
...     f.write('Hello')

ZIP file:
>>> with zipfile.ZipFile('archive.zip', 'w') as z:
...     z.write('file.txt')

===============================================================================
PRACTICE PROGRAMS
===============================================================================

PROGRAM 1: SELECTIVELY COPYING

CHALLENGE:
Write a program that walks through a folder tree and searches for files 
with a certain extension (like .pdf or .jpg). Copy these files from wherever 
they are to a new folder.

REQUIREMENTS:
- Search entire folder tree recursively
- Find all files matching extension
- Copy to centralized folder
- Preserve original filenames

EXAMPLE USE CASE:
Find all PDFs scattered across your Documents folder and copy them to a 
Documents/All_PDFs folder.

HINTS:
- Use os.walk() to traverse folders
- Check file extensions with .endswith() or Path.suffix
- Use shutil.copy() to copy files
- Handle duplicate filenames (maybe add numbers)

STARTER CODE:
```python
import os, shutil
from pathlib import Path

def copy_files_by_extension(source_folder, destination_folder, extension):
    # Create destination folder if it doesn't exist
    # Walk through source folder
    # For each file, check if it matches extension
    # Copy matching files to destination
    pass
```

---

PROGRAM 2: DELETING UNNEEDED FILES

CHALLENGE:
Write a program that finds exceptionally large files (over 100MB) and 
prints their absolute paths. This helps identify what's taking up space 
on your hard drive.

REQUIREMENTS:
- Walk through folder tree
- Check size of each file
- Print files larger than 100MB (104,857,600 bytes)
- Show absolute path and size in MB

EXAMPLE OUTPUT:
```
C:\Users\Al\Videos\movie.mp4 - 523.45 MB
C:\Users\Al\Downloads\game_installer.exe - 1,234.56 MB
```

HINTS:
- Use os.walk() for traversal
- Use Path.stat().st_size for file size
- Convert bytes to MB: size / (1024 ** 2)
- Format output with f-strings

STARTER CODE:
```python
import os
from pathlib import Path

def find_large_files(folder, size_limit_mb=100):
    size_limit_bytes = size_limit_mb * 1024 * 1024
    # Walk through folder
    # Check each file's size
    # Print if larger than limit
    pass
```

---

PROGRAM 3: RENUMBERING FILES

CHALLENGE:
You have files named spam001.txt, spam002.txt, spam003.txt, etc., but 
some numbers are missing (like spam042.txt is deleted). Write a program 
to find gaps and renumber files to close the gaps.

EXAMPLE:
Before: spam001.txt, spam003.txt, spam004.txt (missing spam002.txt)
After:  spam001.txt, spam002.txt, spam003.txt (gap closed)

REQUIREMENTS:
- Find all files with specific prefix
- Detect missing numbers in sequence
- Rename files to close gaps
- Handle three-digit numbering (001, 002, etc.)

HINTS:
- Use glob to find all files matching pattern
- Extract numbers from filenames
- Sort by number
- Rename sequentially

ADVANCED CHALLENGE:
Write a second program that can INSERT gaps (to make room for new files).

---

PROGRAM 4: CONVERTING DATE FORMATS IN FILENAMES

CHALLENGE:
Your boss gives you thousands of files with American-style dates 
(MM-DD-YYYY) in filenames. Convert them to European-style (DD-MM-YYYY).

EXAMPLE:
Before: report_12-31-2023.txt
After:  report_31-12-2023.txt

REQUIREMENTS:
- Search all files in folder and subfolders
- Use regex to find MM-DD-YYYY pattern
- Validate it's a date (not random numbers like 99-99-9999)
- Swap month and day
- Rename file using shutil.move()

REGEX PATTERN HINT:
```python
import re
date_pattern = re.compile(r'(\d{2})-(\d{2})-(\d{4})')
# Group 1: month, Group 2: day, Group 3: year
```

HINTS:
- Use os.walk() to traverse folders
- Use regex to find and capture date parts
- Swap groups: month-day-year → day-month-year
- Use shutil.move() to rename
- Do a dry run first!

VALIDATION:
Check that month is 01-12 and day is 01-31 to avoid matching non-dates.

===============================================================================
END OF CHAPTER 11 SUMMARY
===============================================================================
