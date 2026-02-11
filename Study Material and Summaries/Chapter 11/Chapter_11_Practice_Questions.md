# Chapter 11 Practice Questions

## Questions from Textbook

1. What is the difference between `shutil.copy()` and `shutil.copytree()`?

2. What function is used to rename files?

3. What is the difference between the delete functions in the `send2trash` and `shutil` modules?

4. `ZipFile` objects have a `close()` method just like File objects' `close()` method. What `ZipFile` method is equivalent to File objects' `open()` method?

## Answers

### 1. What is the difference between `shutil.copy()` and `shutil.copytree()`?

**Answer:**
- `shutil.copy()` copies a single file
- `shutil.copytree()` copies an entire folder and all its contents (recursively)

**Detailed Explanation:**

`shutil.copy()`:
- Copies ONE file from source to destination
- Cannot copy folders (only individual files)
- If destination is a folder, file keeps its original name
- If destination is a filename, the file is renamed

Example:
```python
shutil.copy('file.txt', 'backup/')  # Copies to backup/file.txt
shutil.copy('file.txt', 'newname.txt')  # Copies and renames
```

`shutil.copytree()`:
- Copies entire folder tree recursively
- Includes all files, subfolders, and their contents
- Destination folder must NOT already exist
- Perfect for backing up entire directories

Example:
```python
shutil.copytree('project/', 'project_backup/')
```

---

### 2. What function is used to rename files?

**Answer:** `shutil.move()`

**Explanation:**

The `shutil.move()` function is used for renaming because renaming IS moving - you're moving a file to the same folder with a different name.

Renaming example (same folder):
```python
shutil.move('old_name.txt', 'new_name.txt')
```

Moving AND renaming:
```python
shutil.move('folder1/old.txt', 'folder2/new.txt')
```

There is no separate "rename" function in Python. The `shutil.move()` function handles both operations.

---

### 3. What is the difference between the delete functions in the `send2trash` and `shutil` modules?

**Answer:**
- `send2trash`: Sends files to the recycle bin (can be restored)
- `shutil` (and `os`): Permanently deletes files (cannot be restored)

**Detailed Explanation:**

`send2trash.send2trash()`:
- Sends files to recycle bin (Windows) or trash (macOS/Linux)
- Files can be restored if needed
- Safer for testing and development
- Doesn't free disk space until recycle bin is emptied
- Requires installing third-party module: `pip install send2trash`

Example:
```python
import send2trash
send2trash.send2trash('file.txt')  # Safe - can restore from recycle bin
```

`shutil.rmtree()` and `os.unlink()`:
- Permanently deletes files immediately
- Cannot be undone or restored
- Frees disk space right away
- Built into Python (no installation needed)
- Dangerous if used carelessly

Example:
```python
import os
os.unlink('file.txt')  # GONE FOREVER - no recovery!
```

**Best Practice:**
Use `send2trash` during development and testing. Only use permanent deletion when you're absolutely certain.

---

### 4. `ZipFile` objects have a `close()` method just like File objects' `close()` method. What `ZipFile` method is equivalent to File objects' `open()` method?

**Answer:** `zipfile.ZipFile()`

**Explanation:**

For regular files, we use:
- `open()` to create a File object
- `close()` to close it

For ZIP files, we use:
- `zipfile.ZipFile()` to create a ZipFile object (equivalent to `open()`)
- `close()` to close it (same as regular files)

**Comparison:**

Regular file:
```python
file = open('data.txt', 'w', encoding='UTF-8')  # open()
file.write('Hello')
file.close()  # close()
```

ZIP file:
```python
import zipfile
zip_file = zipfile.ZipFile('archive.zip', 'w')  # ZipFile() = equivalent to open()
zip_file.write('file.txt')
zip_file.close()  # close()
```

Both also support `with` statements for automatic closing:

Regular file:
```python
with open('data.txt', 'w', encoding='UTF-8') as f:
    f.write('Hello')
```

ZIP file:
```python
with zipfile.ZipFile('archive.zip', 'w') as z:
    z.write('file.txt')
```
