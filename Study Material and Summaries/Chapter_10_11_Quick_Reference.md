# CHAPTERS 10 & 11 QUICK REFERENCE - MOB PROGRAMMING GUIDE
**Chapters:** Reading/Writing Files (10) & Organizing Files (11)  
**Date:** February 10, 2026

===============================================================================
CHAPTER 10: READING AND WRITING FILES (pathlib)
===============================================================================

## Path Creation & Basics

**Path('folder', 'file.txt')**  
Creates Path object from parts

**Path.home()**  
Gets user's home directory path

**Path.cwd()**  
Gets current working directory path

**path1 / path2**  
Joins paths using / operator

**str(path)**  
Converts Path to string

## Path Attributes

**path.name**  
Gets filename with extension

**path.stem**  
Gets filename without extension

**path.suffix**  
Gets file extension (.txt)

**path.parent**  
Gets parent directory

**path.parts**  
Gets tuple of path components

**path.parents[0], [1], [2]**  
Gets ancestor directories

## Checking Paths

**path.exists()**  
True if path exists

**path.is_file()**  
True if path is file

**path.is_dir()**  
True if path is directory

**path.is_absolute()**  
True if absolute path

**path.absolute()**  
Converts to absolute path

## Reading Files

**path.read_text()**  
Reads entire file as string

**open('file.txt', encoding='UTF-8')**  
Opens file for reading

**file.read()**  
Reads entire file as string

**file.readlines()**  
Reads file as list of lines

**file.close()**  
Closes file (important!)

**with open('file.txt') as file:**  
Opens and auto-closes file

## Writing Files

**path.write_text('content')**  
Writes string to file

**open('file.txt', 'w')**  
Opens file for writing (overwrites)

**open('file.txt', 'a')**  
Opens file for appending

**file.write('text')**  
Writes string to file

## Shelve (Persistent Storage)

**import shelve**  
Import shelve module

**shelf = shelve.open('filename')**  
Opens shelf file

**shelf['key'] = value**  
Stores value with key

**shelf['key']**  
Retrieves value by key

**list(shelf.keys())**  
Gets all keys

**list(shelf.values())**  
Gets all values

**shelf.close()**  
Closes shelf file

===============================================================================
CHAPTER 11: ORGANIZING FILES
===============================================================================

## Copying Files/Folders

**import shutil**  
Import file operations module

**shutil.copy(source, dest)**  
Copies single file

**shutil.copytree(source, dest)**  
Copies entire folder tree

## Moving/Renaming

**shutil.move(source, dest)**  
Moves or renames file/folder

## Deleting Safely

**import send2trash**  
Import safe deletion module

**send2trash.send2trash('file.txt')**  
Moves to recycle bin

## Walking Directory Trees

**import os**  
Import OS module

**os.walk('folder')**  
Generator for directory traversal

**for folder, subfolders, files in os.walk():**  
Loops through directory structure

## Creating ZIP Files

**import zipfile**  
Import ZIP module

**zip = zipfile.ZipFile('name.zip', 'w')**  
Creates new ZIP file

**zip.write('file.txt')**  
Adds file to ZIP

**zip.write('file', compress_type=zipfile.ZIP_DEFLATED)**  
Adds compressed file

**zip.close()**  
Closes ZIP file

## Reading ZIP Files

**zip = zipfile.ZipFile('name.zip')**  
Opens existing ZIP

**zip.namelist()**  
Lists files in ZIP

**zip.getinfo('file.txt')**  
Gets file info object

**info.file_size**  
Original file size

**info.compress_size**  
Compressed file size

**zip.extractall()**  
Extracts all files

**zip.extract('file.txt')**  
Extracts single file

**zip.extract('file.txt', 'folder')**  
Extracts to specific folder

**zip.close()**  
Closes ZIP file

===============================================================================
COMMON PATTERNS
===============================================================================

**Read a file:**
```python
from pathlib import Path
content = Path('file.txt').read_text()
```

**Write a file:**
```python
Path('file.txt').write_text('Hello!')
```

**Loop through file lines:**
```python
with open('file.txt') as file:
    for line in file:
        print(line.strip())
```

**Copy a file:**
```python
import shutil
shutil.copy('original.txt', 'backup.txt')
```

**Move to trash:**
```python
import send2trash
send2trash.send2trash('unwanted.txt')
```

**Create ZIP:**
```python
import zipfile
zip = zipfile.ZipFile('archive.zip', 'w')
zip.write('file.txt')
zip.close()
```

**Extract ZIP:**
```python
zip = zipfile.ZipFile('archive.zip')
zip.extractall()
zip.close()
```

===============================================================================
REMEMBER: Always close files and shelves when done!
Use 'with' statement to auto-close files.
===============================================================================
