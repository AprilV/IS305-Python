# Chapter 10 Practice Questions

## Questions from Textbook

1. What is a relative path relative to?

2. What does an absolute path start with?

3. What does `Path('C:/Users') / 'Al'` evaluate to on Windows?

4. What does `'C:/Users' / 'Al'` evaluate to on Windows?

5. What do the `os.getcwd()` and `os.chdir()` functions do?

6. What are the `.` and `..` folders?

7. In `C:\bacon\eggs\spam.txt`, which part is the directory name, and which part is the base name?

8. What three "mode" arguments can you pass to the `open()` function for plaintext files?

9. What happens if an existing file is opened in write mode?

10. What is the difference between the `read()` and `readlines()` methods?

11. What data structure does a shelf value resemble?

## Answers

### 1. What is a relative path relative to?

**Answer:** The current working directory.

A relative path is relative to the program's current working directory. You can get the current working directory with `Path.cwd()`.

---

### 2. What does an absolute path start with?

**Answer:** The root folder.

- On Windows: `C:\` (or another drive letter like `D:\`)
- On macOS and Linux: `/`

---

### 3. What does `Path('C:/Users') / 'Al'` evaluate to on Windows?

**Answer:** `WindowsPath('C:/Users/Al')`

The `/` operator joins the Path object with the string to create a new Path object.

---

### 4. What does `'C:/Users' / 'Al'` evaluate to on Windows?

**Answer:** This causes a `TypeError`.

Error: `TypeError: unsupported operand type(s) for /: 'str' and 'str'`

Both values are strings. At least one must be a Path object to use the `/` operator.

---

### 5. What do the `os.getcwd()` and `os.chdir()` functions do?

**Answer:**
- `os.getcwd()` returns the current working directory as a string
- `os.chdir()` changes the current working directory

Example:
```python
import os
print(os.getcwd())  # C:\Users\Al
os.chdir('C:\\Windows')
print(os.getcwd())  # C:\Windows
```

---

### 6. What are the `.` and `..` folders?

**Answer:**
- `.` (dot) means "this directory" (the current folder)
- `..` (dot-dot) means "the parent directory" (one folder up)

These are special names you can use in filepaths.

---

### 7. In `C:\bacon\eggs\spam.txt`, which part is the directory name, and which part is the base name?

**Answer:**
- Directory name: `C:\bacon\eggs`
- Base name: `spam.txt`

The directory name is the path to the folder containing the file. The base name is the actual filename.

---

### 8. What three "mode" arguments can you pass to the `open()` function for plaintext files?

**Answer:**
- `'r'` - Read mode (default)
- `'w'` - Write mode (overwrites file)
- `'a'` - Append mode (adds to end of file)

---

### 9. What happens if an existing file is opened in write mode?

**Answer:** The existing file is completely erased and overwritten.

Write mode (`'w'`) deletes all existing content in the file before writing new content. Use append mode (`'a'`) to add to existing content without erasing it.

---

### 10. What is the difference between the `read()` and `readlines()` methods?

**Answer:**
- `read()` returns the entire file contents as a single string
- `readlines()` returns a list of strings, with one string per line

Example:
```python
# read() returns one string
content = file.read()  # 'Line1\nLine2\nLine3'

# readlines() returns a list
lines = file.readlines()  # ['Line1\n', 'Line2\n', 'Line3']
```

---

### 11. What data structure does a shelf value resemble?

**Answer:** A dictionary.

Shelf values have keys and values like dictionaries, and you can use bracket notation and methods like `keys()` and `values()`. The difference is that shelf values are saved to disk.
