===============================================================================
IS 305 - CHAPTER 10: READING AND WRITING FILES - COMPLETE STUDY GUIDE
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

Chapter 10 covers essential file handling operations in Python:
- Understanding files and filepaths (absolute vs relative paths)
- Working with the pathlib module for cross-platform path handling
- Reading and writing plaintext files
- Managing file operations (open, read, write, close)
- Using with statements for automatic file cleanup
- Saving data with the shelve module
- Building practical file automation projects

WHY THIS MATTERS:
Variables store data only while your program runs. To persist data beyond 
program execution, you must save it to files. File operations are fundamental 
to automation tasks like:
- Processing large datasets from text files
- Generating reports and documents
- Backing up and organizing files
- Creating configuration files for applications
- Automating repetitive file management tasks

===============================================================================
FILES AND FILEPATHS - FUNDAMENTAL CONCEPTS
===============================================================================

WHAT IS A FILE?
A file has two key properties:
1. FILENAME - Usually written as one word (e.g., project.docx)
2. PATH - Specifies the location of the file on the computer

ANATOMY OF A FILEPATH:

Example: C:\Users\Al\Documents\project.docx

Breaking it down:
- C:\ = Root folder (the C: drive on Windows)
- Users = Folder inside the root
- Al = Folder inside Users (user's home folder)
- Documents = Folder inside Al
- project.docx = The actual file
  - project = Filename stem (base name)
  - .docx = File extension (tells you the file type)

FILE EXTENSIONS:
The part after the last period tells you what type of file it is:
- .txt = Plain text file
- .pdf = PDF document
- .jpg = JPEG image
- .py = Python script
- .docx = Microsoft Word document

FOLDERS (DIRECTORIES):
Folders can contain:
- Files
- Other folders (called subfolders)
- Both files and folders together

===============================================================================
ROOT FOLDERS ON DIFFERENT OPERATING SYSTEMS
===============================================================================

WINDOWS:
- Root folder: C:\
- Uses backslashes (\) as separators
- Additional drives: D:\, E:\, etc.
- Not case-sensitive (file.txt = FILE.TXT)

Example: C:\Users\Al\Documents\file.txt

macOS:
- Root folder: /
- Uses forward slashes (/) as separators
- Additional volumes appear under /Volumes
- Case-sensitive in newer versions

Example: /Users/Al/Documents/file.txt

LINUX:
- Root folder: /
- Uses forward slashes (/) as separators
- Additional drives appear under /mnt (mount)
- Case-sensitive (file.txt ≠ FILE.TXT)

Example: /home/Al/Documents/file.txt

IMPORTANT NOTE FOR THIS BOOK:
The textbook uses Windows-style examples (C:\), but the Python code uses 
forward slashes (/) because the pathlib module automatically converts them 
to the correct separator for your operating system.

===============================================================================
THE PATHLIB MODULE - CROSS-PLATFORM PATH HANDLING
===============================================================================

WHY USE PATHLIB?
The pathlib module solves the problem of different operating systems using 
different path separators. It provides a Path() function that handles all 
operating systems automatically.

IMPORTING PATHLIB:

from pathlib import Path

This is the standard convention. It lets you type Path() instead of 
pathlib.Path() everywhere in your code.

CREATING PATH OBJECTS:

Basic Usage:
>>> from pathlib import Path
>>> Path('spam', 'bacon', 'eggs')
WindowsPath('spam/bacon/eggs')

WHAT HAPPENED:
- Path() took three separate folder names
- Joined them with the correct separator for your OS
- Returned a Path object (WindowsPath on Windows, PosixPath on macOS/Linux)

CONVERTING TO STRING:

>>> str(Path('spam', 'bacon', 'eggs'))
'spam\\bacon\\eggs'

The str() function converts the Path object to a regular string.
Notice the double backslashes (\\) - Python escapes each backslash.

===============================================================================
JOINING PATHS WITH THE / OPERATOR
===============================================================================

CONCEPT: You can use the / operator to combine Path objects and strings

WHY THIS IS COOL:
Instead of typing out long paths, you can build them piece by piece.

EXAMPLES:

Method 1: Path object / string
>>> from pathlib import Path
>>> Path('spam') / 'bacon' / 'eggs'
WindowsPath('spam/bacon/eggs')

Method 2: Path object / Path object
>>> Path('spam') / Path('bacon/eggs')
WindowsPath('spam/bacon/eggs')

Method 3: Multiple arguments
>>> Path('spam') / Path('bacon', 'eggs')
WindowsPath('spam/bacon/eggs')

CRITICAL RULE:
At least ONE of the first two values must be a Path object!

THIS WORKS:
>>> Path('spam') / 'bacon'  # First value is Path object ✓

THIS DOESN'T WORK:
>>> 'spam' / 'bacon'  # Both are strings ✗
TypeError: unsupported operand type(s) for /: 'str' and 'str'

HOW IT EVALUATES (Left to Right):

Path('spam') / 'bacon' / 'eggs'
    ↓
WindowsPath('spam/bacon') / 'eggs'
    ↓
WindowsPath('spam/bacon/eggs')

FIX FOR THE ERROR:
Put Path() on the left side:
>>> Path('spam') / 'bacon'  # Works!

===============================================================================
CURRENT WORKING DIRECTORY
===============================================================================

CONCEPT: Every running program has a "current working directory"

WHAT IT MEANS:
When you specify a filename without a full path, Python assumes it's in the 
current working directory.

GETTING THE CURRENT WORKING DIRECTORY:

>>> from pathlib import Path
>>> Path.cwd()
WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python313')

HOW IT WORKS:
- Path.cwd() returns a Path object of the current directory
- cwd = "current working directory"
- This is where Python looks for files by default

CHANGING THE CURRENT WORKING DIRECTORY:

>>> import os
>>> os.chdir('C:\\Windows\\System32')
>>> Path.cwd()
WindowsPath('C:/Windows/System32')

WHAT HAPPENED:
1. We imported the os module
2. Used os.chdir() to change directory
3. Verified with Path.cwd() that it changed

IMPORTANT NOTES:
- Use os.chdir() to change directories (no pathlib equivalent)
- Pass the full path as a string
- Use raw strings r'C:\path' or double backslashes 'C:\\path'

ERROR HANDLING:

>>> os.chdir('C:/ThisFolderDoesNotExist')
FileNotFoundError: [WinError 2] The system cannot find the file specified

Python will raise an error if you try to change to a non-existent directory.

PRACTICAL IMPACT:
If current directory is C:\Users\Al\Python313, then:
- filename.txt refers to C:\Users\Al\Python313\filename.txt
- After changing to C:\Windows\System32:
- filename.txt now refers to C:\Windows\System32\filename.txt

===============================================================================
HOME DIRECTORY
===============================================================================

CONCEPT: Every user has a personal folder called the "home directory"

WHY IT MATTERS:
- Your programs almost always have permission to read/write here
- It's the ideal place for your Python programs to store files
- Different from the current working directory

ACCESSING THE HOME DIRECTORY:

>>> from pathlib import Path
>>> Path.home()
WindowsPath('C:/Users/Al')

HOME DIRECTORY LOCATIONS BY OS:

Windows:  C:\Users\<username>
macOS:    /Users/<username>
Linux:    /home/<username>

PRACTICAL USE:

>>> from pathlib import Path
>>> my_file = Path.home() / 'my_data.txt'
>>> print(my_file)
C:\Users\Al\my_data.txt

This ensures your file goes in a safe, accessible location.

===============================================================================
ABSOLUTE VS RELATIVE PATHS
===============================================================================

ABSOLUTE PATH:
Definition: Always begins with the root folder
- Windows: Starts with C:\ (or D:\, E:\, etc.)
- macOS/Linux: Starts with /

Examples:
Windows:  C:\Users\Al\Documents\file.txt
macOS:    /Users/Al/Documents/file.txt
Linux:    /home/Al/Documents/file.txt

RELATIVE PATH:
Definition: Relative to the program's current working directory
- Does NOT start with the root folder
- Depends on where your program is currently running

Examples:
spam\eggs\file.txt
.\Documents\file.txt
..\parent_folder\file.txt

SPECIAL FOLDER NAMES:

. (single dot) = "This folder" (current folder)
.. (dot-dot) = "Parent folder" (one level up)

VISUAL EXAMPLE:

If current working directory is C:\bacon:

C:\bacon\
  ├── spam.txt           → .\spam.txt  or  spam.txt
  └── eggs\
      └── file.txt       → .\eggs\file.txt  or  eggs\file.txt

C:\                      → ..\..\  (parent of parent)
  └── Users\             → ..\Users\  (parent's sibling)

IMPORTANT NOTE:
The .\ at the start is optional:
.\spam.txt = spam.txt (both mean the same thing)

CHECKING IF A PATH IS ABSOLUTE:

>>> from pathlib import Path
>>> Path.cwd()
WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python312')
>>> Path.cwd().is_absolute()
True
>>> Path('spam/bacon/eggs').is_absolute()
False

CONVERTING RELATIVE TO ABSOLUTE:

Method 1: Using Path.cwd()
>>> Path.cwd() / Path('my/relative/path')
WindowsPath('C:/Users/Al/Desktop/my/relative/path')

Method 2: Using absolute() method
>>> Path('my/relative/path').absolute()
WindowsPath('C:/Users/Al/Desktop/my/relative/path')

Method 3: Relative to home directory
>>> Path.home() / Path('my/relative/path')
WindowsPath('C:/Users/Al/my/relative/path')

===============================================================================
CREATING NEW FOLDERS
===============================================================================

METHOD 1: os.makedirs() - Creates all intermediate folders

>>> import os
>>> os.makedirs('C:\\delicious\\walnut\\waffles')

WHAT IT DOES:
- Creates C:\delicious
- Creates C:\delicious\walnut
- Creates C:\delicious\walnut\waffles
- All in one command!

Result:
C:\
└── delicious\
    └── walnut\
        └── waffles\

METHOD 2: Path.mkdir() - Creates one directory

>>> from pathlib import Path
>>> Path(r'C:\Users\Al\spam').mkdir()

LIMITATION:
This only creates ONE directory at a time. Parent folders must already exist.

SOLUTION - Use parents=True:

>>> Path(r'C:\Users\Al\spam\eggs\bacon').mkdir(parents=True)

Now it works like os.makedirs() - creates all necessary parent folders.

IMPORTANT NOTES:
- mkdir() will raise an error if the folder already exists
- Use exist_ok=True to avoid this error:
  >>> Path('spam').mkdir(exist_ok=True)

===============================================================================
GETTING PARTS OF A FILEPATH
===============================================================================

Path objects have attributes to extract different parts of the filepath.

EXAMPLE PATH (Windows):
C:\Users\Al\spam.txt

EXAMPLE PATH (macOS/Linux):
/Users/Al/spam.txt

PATH ATTRIBUTES:

>>> from pathlib import Path
>>> p = Path('C:/Users/Al/spam.txt')

>>> p.anchor
'C:\\'
The root folder of the filesystem

>>> p.parent
WindowsPath('C:/Users/Al')
The folder that contains the file (returns Path object)

>>> p.name
'spam.txt'
The file's full name (stem + suffix)

>>> p.stem
'spam'
The base name without the extension

>>> p.suffix
'.txt'
The file extension (includes the dot)

>>> p.drive
'C:'
The drive letter (Windows only; empty on macOS/Linux)

VISUAL BREAKDOWN:

Windows:
C:\Users\Al\spam.txt
│  │      │  │   │
│  │      │  │   └─ suffix: '.txt'
│  │      │  └───── stem: 'spam'
│  │      └──────── name: 'spam.txt'
│  └─────────────── parent: WindowsPath('C:/Users/Al')
└────────────────── anchor: 'C:\\'
                    drive: 'C:'

macOS/Linux:
/Users/Al/spam.txt
│ │      │  │   │
│ │      │  │   └─ suffix: '.txt'
│ │      │  └───── stem: 'spam'
│ │      └──────── name: 'spam.txt'
│ └─────────────── parent: PosixPath('/Users/Al')
└────────────────── anchor: '/'
                    drive: '' (empty on macOS/Linux)

GETTING PATH AS TUPLE OF PARTS:

>>> p.parts
('C:\\', 'Users', 'Al', 'spam.txt')

You can access individual parts by index:
>>> p.parts[3]
'spam.txt'
>>> p.parts[0:2]
('C:\\', 'Users')

ACCESSING ANCESTOR FOLDERS (parents attribute):

>>> Path.cwd()
WindowsPath('C:/Users/Al/Desktop')
>>> Path.cwd().parents[0]
WindowsPath('C:/Users/Al')
>>> Path.cwd().parents[1]
WindowsPath('C:/Users')
>>> Path.cwd().parents[2]
WindowsPath('C:/')

How it works:
parents[0] = immediate parent (one level up)
parents[1] = grandparent (two levels up)
parents[2] = great-grandparent (three levels up)
...and so on until you reach the root folder

===============================================================================
FILE SIZES AND TIMESTAMPS
===============================================================================

The stat() method returns information about a file's size and timestamps.

BASIC USAGE:

>>> from pathlib import Path
>>> calc_file = Path('C:/Windows/System32/calc.exe')
>>> calc_file.stat()
os.stat_result(st_mode=33279, st_ino=562949956525418, st_dev=3739257218,
st_nlink=2, st_uid=0, st_gid=0, st_size=27648, st_atime=1678984560,
st_mtime=1575709787, st_ctime=1575709787)

USEFUL ATTRIBUTES:

FILE SIZE:
>>> calc_file.stat().st_size
27648

This is in bytes. To convert:
- KB: divide by 1024
- MB: divide by 1024 ** 2
- GB: divide by 1024 ** 3

Example:
>>> size_kb = calc_file.stat().st_size / 1024
>>> size_mb = calc_file.stat().st_size / (1024 ** 2)

LAST MODIFIED TIMESTAMP:
>>> calc_file.stat().st_mtime
1712627129.0906117

This is Unix epoch time (seconds since January 1, 1970).

CONVERTING TO HUMAN-READABLE FORMAT:

>>> import time
>>> time.asctime(time.localtime(calc_file.stat().st_mtime))
'Mon Apr  8 20:45:29 2024'

COMPLETE LIST OF stat_result ATTRIBUTES:

st_size      File size in bytes
st_mtime     Last modified timestamp
st_ctime     Creation timestamp (Windows) or metadata change time (macOS/Linux)
st_atime     Last accessed timestamp

PRACTICAL EXAMPLE - Find large files:

>>> for file in Path.home().glob('*.txt'):
...     size_mb = file.stat().st_size / (1024 ** 2)
...     if size_mb > 10:
...         print(f'{file.name}: {size_mb:.2f} MB')

IMPORTANT WARNING:
Timestamps can be manually changed and may not always be accurate.

===============================================================================
GLOB PATTERNS - FINDING FILES WITH WILDCARDS
===============================================================================

CONCEPT: Glob patterns use * and ? as wildcards to match filenames

WILDCARD CHARACTERS:

* (asterisk) = Matches any text (zero or more characters)
? (question mark) = Matches exactly one character

GLOB PATTERN EXAMPLES:

'*.txt'
Matches: report.txt, data.txt, notes.txt
Doesn't match: image.jpg, script.py

'project?.txt'
Matches: project1.txt, project2.txt, projectX.txt
Doesn't match: project10.txt (? matches only ONE character)

'*project?.*'
Matches: catproject5.txt, secret_project7.docx
Doesn't match: project.txt (needs at least one char before 'project')

'*'
Matches: ALL files and folders

USING glob() METHOD:

>>> from pathlib import Path
>>> p = Path('C:/Users/Al/Desktop')
>>> p.glob('*')
<generator object Path.glob at 0x000002A6E389DED0>

The glob() method returns a generator object. Convert to list to see results:

>>> list(p.glob('*'))
[WindowsPath('C:/Users/Al/Desktop/1.png'),
 WindowsPath('C:/Users/Al/Desktop/22-ap.pdf'),
 WindowsPath('C:/Users/Al/Desktop/cat.jpg'),
 WindowsPath('C:/Users/Al/Desktop/zzz.txt')]

USING IN A FOR LOOP:

>>> for file in Path('C:/Users/Al/Desktop').glob('*.txt'):
...     print(file)
...
C:\Users\Al\Desktop\zzz.txt
C:\Users\Al\Desktop\notes.txt
C:\Users\Al\Desktop\readme.txt

PRACTICAL USE CASES:

Find all Python files:
>>> for py_file in Path.home().glob('*.py'):
...     print(py_file.name)

Find all images:
>>> for img in Path('photos').glob('*.jpg'):
...     # Process each image
...     pass

Backup all documents:
>>> for doc in Path('Documents').glob('*.docx'):
...     # Copy to backup folder
...     pass

===============================================================================
CHECKING PATH VALIDITY
===============================================================================

Before working with files, check if they exist to avoid errors.

PATH VALIDATION METHODS:

exists()   Returns True if path exists, False otherwise
is_file()  Returns True if path exists AND is a file
is_dir()   Returns True if path exists AND is a directory

EXAMPLES:

>>> from pathlib import Path
>>> win_dir = Path('C:/Windows')
>>> not_exists_dir = Path('C:/This/Folder/Does/Not/Exist')
>>> calc_file = Path('C:/Windows/System32/calc.exe')

>>> win_dir.exists()
True
>>> win_dir.is_dir()
True

>>> not_exists_dir.exists()
False

>>> calc_file.is_file()
True
>>> calc_file.is_dir()
False

CHECKING FOR REMOVABLE DRIVES:

>>> d_drive = Path('D:/')
>>> d_drive.exists()
False

This tells us there's no D: drive currently attached.

PRACTICAL USE - SAFE FILE OPERATIONS:

Before reading:
>>> file = Path('data.txt')
>>> if file.is_file():
...     content = file.read_text()
... else:
...     print('File not found!')

Before creating a folder:
>>> folder = Path('new_folder')
>>> if not folder.exists():
...     folder.mkdir()

WHY THIS MATTERS:
Functions will crash with errors if you pass a non-existent path.
Always validate paths before performing operations on them.

===============================================================================
PLAINTEXT VS BINARY FILES
===============================================================================

PLAINTEXT FILES:
- Contain only basic text characters
- No font, size, or color information
- Can be opened with Notepad or TextEdit
- Easily read as strings in Python

Examples:
- .txt files
- .py Python scripts
- .csv data files
- .md Markdown files

BINARY FILES:
- All other file types
- Contain special formatting and data
- Look like gibberish in a text editor
- Must be handled with special modules

Examples:
- .docx Word documents
- .pdf PDF files
- .jpg/.png images
- .xlsx Excel spreadsheets
- .exe executable programs

WHAT BINARY LOOKS LIKE IN NOTEPAD:
If you open calc.exe in Notepad, you'll see scrambled nonsense like:
MZÿÿ¸@º´ Í!¸LÍ!This program cannot be run in DOS mode...

WHY THE DISTINCTION MATTERS:
- Plaintext files: Use open(), read(), write()
- Binary files: Use special modules (like shelve, openpyxl, Pillow)

This chapter focuses on plaintext files.

===============================================================================
SIMPLE FILE READING AND WRITING WITH PATHLIB
===============================================================================

Path objects have simple methods for basic file operations.

WRITING TO A FILE:

>>> from pathlib import Path
>>> p = Path('spam.txt')
>>> p.write_text('Hello, world!')
13

WHAT HAPPENED:
- Created a new file spam.txt (or overwrote existing one)
- Wrote 'Hello, world!' to it
- Returned 13 (number of characters written)

READING FROM A FILE:

>>> p.read_text()
'Hello, world!'

Returns the entire file contents as one string.

IMPORTANT NOTES:
- write_text() OVERWRITES the file if it already exists
- These methods are simple but limited
- For more control, use open() and File objects (covered next)

===============================================================================
THE FILE READING/WRITING PROCESS (THREE STEPS)
===============================================================================

STANDARD WORKFLOW:

1. Call open() to get a File object
2. Call read() or write() on the File object
3. Call close() on the File object

This is more flexible than write_text()/read_text().

===============================================================================
OPENING FILES
===============================================================================

BASIC SYNTAX:

>>> from pathlib import Path
>>> hello_file = open(Path.home() / 'hello.txt', encoding='UTF-8')

WHAT THIS DOES:
- Opens hello.txt in the home directory
- Opens in READ MODE (default)
- Returns a File object stored in hello_file
- Specifies UTF-8 encoding

FILE MODES:

'r'  Read mode (default) - Can only read, not write
'w'  Write mode - Creates new file or OVERWRITES existing
'a'  Append mode - Adds to the end of existing file

SPECIFYING MODE EXPLICITLY:

>>> file = open('hello.txt', 'r', encoding='UTF-8')  # Read mode
>>> file = open('output.txt', 'w', encoding='UTF-8')  # Write mode
>>> file = open('log.txt', 'a', encoding='UTF-8')  # Append mode

ABOUT ENCODING:

UTF-8 is the standard encoding for text files.
- macOS and Linux use UTF-8 by default
- Windows uses 'cp1252' by default (can cause problems!)

BEST PRACTICE: Always specify encoding='UTF-8' when opening plaintext files.

>>> file = open('data.txt', encoding='UTF-8')  # Good!
>>> file = open('data.txt')  # May fail on Windows with non-English characters

THE FILE OBJECT:

>>> hello_file
<_io.TextIOWrapper name='C:\\Users\\Al\\hello.txt' mode='r' encoding='UTF-8'>

This is a File object - a new type of value, like lists and dictionaries.
You call methods on it to read or write.

===============================================================================
READING FILE CONTENTS
===============================================================================

METHOD 1: read() - Returns entire file as one string

Create hello.txt with this content:
Hello, world!

Then:
>>> hello_file = open(Path.home() / 'hello.txt', encoding='UTF-8')
>>> hello_content = hello_file.read()
>>> hello_content
'Hello, world!'
>>> hello_file.close()

WHAT HAPPENED:
- Opened the file
- read() returned all contents as a single string
- Stored in hello_content variable
- Closed the file

METHOD 2: readlines() - Returns list of strings, one per line

Create sonnet29.txt with this content:
When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,

Then:
>>> sonnet_file = open(Path.home() / 'sonnet29.txt', encoding='UTF-8')
>>> sonnet_file.readlines()
["When, in disgrace with fortune and men's eyes,\n",
 'I all alone beweep my outcast state,\n',
 'And trouble deaf heaven with my bootless cries,\n',
 'And look upon myself and curse my fate,']
>>> sonnet_file.close()

WHAT HAPPENED:
- Each line became a string in a list
- Each string ends with \n (newline character)
- Except the last line (no newline at end of file)

WHEN TO USE EACH:

read()      When you want entire file as one big string
readlines() When you want to process file line by line

IMPORTANT: Always close the file when done!

===============================================================================
WRITING TO FILES
===============================================================================

YOU CANNOT WRITE TO A FILE OPENED IN READ MODE!

Must open in write mode ('w') or append mode ('a'):

WRITE MODE ('w'):
- OVERWRITES existing file completely
- Creates new file if it doesn't exist
- Like replacing a variable's value

APPEND MODE ('a'):
- ADDS to the end of existing file
- Creates new file if it doesn't exist
- Like appending to a list

EXAMPLE - Write and Append:

>>> bacon_file = open('bacon.txt', 'w', encoding='UTF-8')
>>> bacon_file.write('Hello, world!\n')
14
>>> bacon_file.close()

>>> bacon_file = open('bacon.txt', 'a', encoding='UTF-8')
>>> bacon_file.write('Bacon is not a vegetable.')
25
>>> bacon_file.close()

>>> bacon_file = open('bacon.txt', encoding='UTF-8')
>>> content = bacon_file.read()
>>> bacon_file.close()
>>> print(content)
Hello, world!
Bacon is not a vegetable.

STEP-BY-STEP BREAKDOWN:

Step 1: Open in write mode, write first line
'w' mode creates the file
write() returns 14 (characters written, including \n)
close() saves and closes

Step 2: Open in append mode, add second line
'a' mode adds to existing content
write() returns 25 (characters in second string)
close() saves and closes

Step 3: Read the final result
Default 'r' mode to read
read() gets entire contents
Shows both lines combined

CRITICAL NOTE ABOUT write():
Unlike print(), write() does NOT add a newline automatically!

>>> file.write('Line 1')
>>> file.write('Line 2')
Results in: Line 1Line 2 (no line break!)

You must add \n yourself:
>>> file.write('Line 1\n')
>>> file.write('Line 2\n')
Results in:
Line 1
Line 2

===============================================================================
USING WITH STATEMENTS - AUTOMATIC FILE CLEANUP
===============================================================================

THE PROBLEM:
You might forget to call close(), or your program might crash before reaching 
the close() call, leaving files open.

THE SOLUTION: with statements

CONCEPT: A with statement automatically closes the file when done, even if 
an error occurs.

OLD WAY (Manual close):

file_obj = open('data.txt', 'w', encoding='UTF-8')
file_obj.write('Hello, world!')
file_obj.close()

file_obj = open('data.txt', encoding='UTF-8')
content = file_obj.read()
file_obj.close()

NEW WAY (Automatic close with 'with'):

with open('data.txt', 'w', encoding='UTF-8') as file_obj:
    file_obj.write('Hello, world!')

with open('data.txt', encoding='UTF-8') as file_obj:
    content = file_obj.read()

WHAT HAPPENED:
- No close() calls needed!
- Python automatically closes when exiting the indented block
- Even if an error occurs, the file gets closed properly

HOW IT WORKS:

1. with statement creates a "context manager"
2. The indented block is where you work with the file
3. When execution leaves the block, Python automatically closes the file
4. This happens no matter how you exit (return, error, etc.)

SYNTAX BREAKDOWN:

with open('filename', 'mode', encoding='UTF-8') as variable_name:
    # Indented block - file is open here
    variable_name.write('data')
    # File automatically closes when block ends

# File is now closed - cannot use variable_name anymore

MULTIPLE FILES:

with open('input.txt', encoding='UTF-8') as in_file:
    with open('output.txt', 'w', encoding='UTF-8') as out_file:
        content = in_file.read()
        out_file.write(content.upper())

BEST PRACTICE:
Always use with statements when working with files!
It's safer and cleaner than manual close() calls.

===============================================================================
SAVING VARIABLES WITH THE shelve MODULE
===============================================================================

CONCEPT: Save Python variables to files so they persist between program runs

WHY USE shelve:
- Save program configuration settings
- Store game save data
- Keep user preferences
- Persist any Python data between runs

THINK OF IT AS:
Adding "Save" and "Load" features to your programs

CREATING A SHELF FILE:

>>> import shelve
>>> shelf_file = shelve.open('mydata')
>>> shelf_file['cats'] = ['Zophie', 'Pooka', 'Simon']
>>> shelf_file.close()

WHAT HAPPENED:
1. shelve.open('mydata') creates shelf files (mydata.bak, mydata.dat, mydata.dir on Windows)
2. Use shelf like a dictionary: shelf_file['key'] = value
3. close() saves everything

FILE TYPES CREATED:

Windows: Creates three files
- mydata.bak
- mydata.dat
- mydata.dir

macOS: Creates one file
- mydata.db

Linux: Creates one file
- mydata

You don't need to understand the file format - shelve handles it!

READING FROM A SHELF FILE:

>>> shelf_file = shelve.open('mydata')
>>> type(shelf_file)
<class 'shelve.DbfilenameShelf'>
>>> shelf_file['cats']
['Zophie', 'Pooka', 'Simon']
>>> shelf_file.close()

WHAT HAPPENED:
- Opened the existing shelf files
- Retrieved the data just like from a dictionary
- Got back the exact list we stored earlier

SHELF FILES WORK LIKE DICTIONARIES:

Getting keys and values:
>>> shelf_file = shelve.open('mydata')
>>> list(shelf_file.keys())
['cats']
>>> list(shelf_file.values())
[['Zophie', 'Pooka', 'Simon']]
>>> shelf_file.close()

IMPORTANT NOTES:
- Shelf values allow both reading AND writing once opened
- No need to specify 'r' or 'w' mode like with text files
- Data is stored in binary format (not human-readable)
- Perfect for saving Python data structures (lists, dicts, etc.)

PLAINTEXT VS SHELVE:

Use plaintext (.txt files):
- When you'll edit files in Notepad/TextEdit
- When other programs need to read the files
- When human-readability matters

Use shelve:
- When saving Python program data
- When you need to store lists, dictionaries, etc.
- When you want easy Save/Load functionality

===============================================================================
PRACTICAL PROJECT: RANDOM QUIZ GENERATOR
===============================================================================

PROBLEM:
You're a teacher with 35 students. You want to create unique quizzes for each 
student with randomized questions and answer choices to prevent cheating.

MANUAL APPROACH: Would take hours or days

AUTOMATED APPROACH: Python can do it in seconds!

WHAT THE PROGRAM DOES:
1. Creates 35 different quiz files
2. Each quiz has 50 multiple-choice questions in random order
3. Each question has the correct answer plus 3 random wrong answers
4. Answer choices are in random order
5. Creates answer key files for grading

TECHNICAL REQUIREMENTS:
- Store states/capitals in a dictionary
- Use open(), write(), close() for files
- Use random.shuffle() to randomize order
- Generate unique filenames for each quiz

STEP 1: STORE QUIZ DATA

import random

capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    # ... all 50 states
    'Wyoming': 'Cheyenne'
}

for quiz_num in range(35):
    # Create 35 quizzes
    pass

STEP 2: CREATE QUIZ FILES

for quiz_num in range(35):
    # Create unique filenames
    quiz_file = open(f'capitalsquiz{quiz_num + 1}.txt', 'w', encoding='UTF-8')
    answer_file = open(f'capitalsquiz_answers{quiz_num + 1}.txt', 'w', encoding='UTF-8')
    
    # Write header
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' ' * 20) + f'State Capitals Quiz (Form {quiz_num + 1})')
    quiz_file.write('\n\n')
    
    # Randomize state order
    states = list(capitals.keys())
    random.shuffle(states)

WHY {quiz_num + 1}:
quiz_num goes 0, 1, 2, ... but we want filenames to be 1, 2, 3, ...

STEP 3: CREATE ANSWER OPTIONS

for num in range(50):
    # Get correct answer
    correct_answer = capitals[states[num]]
    
    # Create list of wrong answers
    wrong_answers = list(capitals.values())
    del wrong_answers[wrong_answers.index(correct_answer)]
    wrong_answers = random.sample(wrong_answers, 3)
    
    # Combine and shuffle all options
    answer_options = wrong_answers + [correct_answer]
    random.shuffle(answer_options)

HOW IT WORKS:
1. correct_answer = the right capital for this state
2. wrong_answers = all capitals except the correct one
3. random.sample() picks 3 random wrong answers
4. Combine and shuffle so correct answer isn't always in same position

STEP 4: WRITE QUESTIONS AND ANSWERS

for num in range(50):
    # ... (answer creation code from Step 3)
    
    # Write question
    quiz_file.write(f'{num + 1}. What is the capital of {states[num]}?\n')
    
    # Write answer choices
    for i in range(4):
        quiz_file.write(f"    {'ABCD'[i]}. {answer_options[i]}\n")
    quiz_file.write('\n')
    
    # Write answer key
    answer_file.write(f"{num + 1}. {'ABCD'[answer_options.index(correct_answer)]}\n")

quiz_file.close()
answer_file.close()

CLEVER TRICKS:

'ABCD'[i] treats string as array:
i = 0 → 'A'
i = 1 → 'B'
i = 2 → 'C'
i = 3 → 'D'

answer_options.index(correct_answer):
Finds which position (0-3) has the correct answer
Then 'ABCD'[position] gives the letter

SAMPLE OUTPUT (capitalsquiz1.txt):

Name:

Date:

Period:

                    State Capitals Quiz (Form 1)

1. What is the capital of West Virginia?
    A. Hartford
    B. Santa Fe
    C. Harrisburg
    D. Charleston

2. What is the capital of Colorado?
    A. Raleigh
    B. Harrisburg
    C. Denver
    D. Lincoln

SAMPLE ANSWER KEY (capitalsquiz_answers1.txt):

1. D
2. C
3. A
...

THE POWER OF AUTOMATION:
- Manual creation: Hours or days
- Python script: Seconds
- Works for ANY multiple-choice quiz format!

===============================================================================
CHAPTER SUMMARY
===============================================================================

KEY CONCEPTS LEARNED:

1. FILES AND PATHS
   - Files have names and paths
   - Paths can be absolute (from root) or relative (from current directory)
   - Different OS use different separators (\ vs /)

2. PATHLIB MODULE
   - Path() creates cross-platform path objects
   - Use / operator to join paths
   - Path.cwd() gets current working directory
   - Path.home() gets user's home folder

3. PATH MANIPULATION
   - .parent, .name, .stem, .suffix extract path parts
   - .exists(), .is_file(), .is_dir() check validity
   - .glob() finds files matching patterns
   - .stat() gets file size and timestamps

4. FILE OPERATIONS
   - open() creates File objects
   - read() returns entire file as string
   - readlines() returns list of lines
   - write() writes to file (no automatic newline!)
   - Always close files or use with statements

5. FILE MODES
   - 'r' = read (default)
   - 'w' = write (overwrites!)
   - 'a' = append (adds to end)

6. BEST PRACTICES
   - Use with statements for automatic cleanup
   - Always specify encoding='UTF-8'
   - Validate paths before operations
   - Use shelve for saving Python variables

7. AUTOMATION POTENTIAL
   - Can process thousands of files quickly
   - Create reports and documents programmatically
   - Generate customized content at scale

===============================================================================
PRACTICE QUESTIONS WITH DETAILED ANSWERS
===============================================================================

1. What is a relative path relative to?

ANSWER: A relative path is relative to the program's current working directory.

EXPLANATION:
When you use a relative path like 'spam.txt' or 'folder/file.txt', Python 
interprets it based on the current working directory. If the current working 
directory is C:\Users\Al\Documents, then:
- 'spam.txt' refers to C:\Users\Al\Documents\spam.txt
- 'folder/file.txt' refers to C:\Users\Al\Documents\folder\file.txt

You can find the current working directory with Path.cwd().

---

2. What does an absolute path start with?

ANSWER: An absolute path starts with the root folder.

EXPLANATION:
- Windows: C:\ (or D:\, E:\, etc.)
- macOS/Linux: /

Examples of absolute paths:
- Windows: C:\Users\Al\Documents\file.txt
- macOS: /Users/Al/Documents/file.txt
- Linux: /home/Al/Documents/file.txt

The key is that absolute paths always start from the very top (root) of 
the filesystem, so they work regardless of the current working directory.

---

3. What does Path('C:/Users') / 'Al' evaluate to on Windows?

ANSWER: WindowsPath('C:/Users/Al')

EXPLANATION:
The / operator joins paths together. Since the left side is a Path object 
(created by Path('C:/Users')), the operation succeeds and creates a new 
Path object representing C:\Users\Al. Even though we used forward slashes 
in the code, Windows will interpret this correctly because pathlib handles 
the conversion.

---

4. What does 'C:/Users' / 'Al' evaluate to on Windows?

ANSWER: This causes a TypeError

EXPLANATION:
TypeError: unsupported operand type(s) for /: 'str' and 'str'

Both sides are strings, not Path objects. The / operator only works when 
at least one side is a Path object. To fix this, make the left side a 
Path object:

Correct: Path('C:/Users') / 'Al'

---

5. What do the os.getcwd() and os.chdir() functions do?

ANSWER:
- os.getcwd() returns the current working directory as a string
- os.chdir() changes the current working directory

EXPLANATION:

os.getcwd() (get current working directory):
>>> import os
>>> os.getcwd()
'C:\\Users\\Al\\Python313'

Returns where your program is currently "located" in the filesystem.

os.chdir(path) (change directory):
>>> os.chdir('C:\\Windows\\System32')
>>> os.getcwd()
'C:\\Windows\\System32'

Changes where Python looks for files by default.

NOTE: The modern equivalent of os.getcwd() is Path.cwd(), which returns 
a Path object instead of a string. However, there's no pathlib equivalent 
for os.chdir() - you must use the os module to change directories.

---

6. What are the . and .. folders?

ANSWER:
- . (dot) = the current folder ("this folder")
- .. (dot-dot) = the parent folder ("one level up")

EXPLANATION:

. (current folder):
If you're in C:\Users\Al\Documents:
.\file.txt is the same as C:\Users\Al\Documents\file.txt
Just means "file.txt in this folder"

.. (parent folder):
If you're in C:\Users\Al\Documents:
..\file.txt refers to C:\Users\Al\file.txt
Goes one level up to the parent folder

You can chain them:
..\..\file.txt goes up two levels
.\folder\file.txt goes into a subfolder

These are not real folders - they're special names that work in any directory.

---

7. In C:\bacon\eggs\spam.txt, which part is the directory name, and which 
part is the base name?

ANSWER:
- Directory name (path): C:\bacon\eggs
- Base name (filename): spam.txt

EXPLANATION:
The directory name is everything except the final file:
C:\bacon\eggs (the folder containing the file)

The base name is just the filename itself:
spam.txt

In pathlib terms:
>>> p = Path('C:/bacon/eggs/spam.txt')
>>> p.parent
WindowsPath('C:/bacon/eggs')  # Directory
>>> p.name
'spam.txt'  # Base name
>>> p.stem
'spam'  # Base name without extension

---

8. What three "mode" arguments can you pass to the open() function for 
plaintext files?

ANSWER:
- 'r' = Read mode
- 'w' = Write mode
- 'a' = Append mode

EXPLANATION:

'r' (Read mode - default):
>>> file = open('data.txt', 'r', encoding='UTF-8')
- Can only read the file, not modify it
- File must already exist (error if it doesn't)
- This is the default if you don't specify a mode

'w' (Write mode):
>>> file = open('output.txt', 'w', encoding='UTF-8')
- Creates a new file if it doesn't exist
- OVERWRITES the entire file if it does exist
- Use when creating new files or replacing content

'a' (Append mode):
>>> file = open('log.txt', 'a', encoding='UTF-8')
- Creates a new file if it doesn't exist
- ADDS to the end if file exists (doesn't overwrite)
- Use for log files or adding to existing content

---

9. What happens if an existing file is opened in write mode?

ANSWER: The file is completely erased and overwritten with new content.

EXPLANATION:
Write mode ('w') is destructive! All existing content is deleted.

Example:
Suppose data.txt contains:
Line 1
Line 2
Line 3

Then you run:
>>> file = open('data.txt', 'w', encoding='UTF-8')
>>> file.write('New content')
>>> file.close()

Now data.txt contains only:
New content

All previous content ('Line 1\nLine 2\nLine 3') is GONE!

TO AVOID DATA LOSS:
- Use 'a' (append mode) to add to existing content
- Make backups before using write mode
- Use 'r+' if you need to read and write (advanced)

---

10. What is the difference between the read() and readlines() methods?

ANSWER:
- read() returns the entire file as ONE string
- readlines() returns a LIST of strings, one per line

EXPLANATION:

read() example:
File content:
Line 1
Line 2
Line 3

>>> file = open('data.txt', encoding='UTF-8')
>>> content = file.read()
>>> content
'Line 1\nLine 2\nLine 3'
>>> type(content)
<class 'str'>

Returns one big string with \n newline characters.

readlines() example:
Same file content:
>>> file = open('data.txt', encoding='UTF-8')
>>> lines = file.readlines()
>>> lines
['Line 1\n', 'Line 2\n', 'Line 3']
>>> type(lines)
<class 'list'>

Returns a list where each element is one line (with \n except last line).

WHEN TO USE EACH:

Use read():
- When you want the whole file as text
- When file size is manageable
- When processing entire content at once

Use readlines():
- When processing line by line
- When you need to iterate over lines
- When you need line numbers

>>> for line in file.readlines():
...     process(line)

---

11. What data structure does a shelf value resemble?

ANSWER: A shelf value resembles a dictionary.

EXPLANATION:

Dictionaries:
>>> my_dict = {'key1': 'value1', 'key2': 'value2'}
>>> my_dict['key1']
'value1'
>>> my_dict.keys()
dict_keys(['key1', 'key2'])

Shelf values:
>>> import shelve
>>> shelf_file = shelve.open('mydata')
>>> shelf_file['key1'] = 'value1'
>>> shelf_file['key2'] = 'value2'
>>> shelf_file['key1']
'value1'
>>> shelf_file.keys()
KeysView(<shelve.DbfilenameShelf object>)

SIMILARITIES:
- Use bracket notation: shelf['key']
- Have keys() and values() methods
- Store key-value pairs
- Can use any string as a key

KEY DIFFERENCE:
Shelf values save to disk (persist between programs), while dictionaries 
only exist in memory while the program runs.

Think of shelve as a "dictionary that saves itself to a file automatically."

===============================================================================
PRACTICE PROGRAMS
===============================================================================

PROGRAM 1: MAD LIBS

CHALLENGE:
Create a program that reads text files and replaces ADJECTIVE, NOUN, ADVERB, 
and VERB with user input.

INPUT FILE (template.txt):
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.

PROGRAM INTERACTION:
Enter an adjective: silly
Enter a noun: chandelier
Enter a verb: screamed
Enter a noun: pickup truck

OUTPUT FILE:
The silly panda walked to the chandelier and then screamed. A nearby
pickup truck was unaffected by these events.

REQUIREMENTS:
- Print results to screen
- Save to new text file
- Prompt user for each replacement

HINTS:
- Use read() to get file contents as string
- Use replace() or regex to find placeholders
- Use input() to get user's words
- Use write() to save result

---

PROGRAM 2: REGEX SEARCH

CHALLENGE:
Write a program that searches all .txt files in a folder for lines matching 
a user-supplied regular expression.

REQUIREMENTS:
- Open all .txt files in a folder
- Search each line for the regex pattern
- Print matching lines to screen

EXAMPLE:
User enters regex: \d{3}-\d{3}-\d{4}
Program finds and prints all lines containing phone numbers

HINTS:
- Use Path.glob('*.txt') to find all .txt files
- Use re.compile() for the regex
- Use readlines() to process line by line
- Print filename and line number with each match

===============================================================================
END OF CHAPTER 10 SUMMARY
===============================================================================
