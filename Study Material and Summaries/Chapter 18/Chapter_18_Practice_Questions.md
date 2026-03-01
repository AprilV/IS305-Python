# Chapter 18 Practice Questions

## Questions

1. What are some features Excel spreadsheets have that CSV spreadsheets don't?

2. What do you pass to `csv.reader()` and `csv.writer()` to create reader and writer objects?

3. What modes do File objects for reader and writer objects need to be opened in?

4. What method takes a list argument and writes it to a CSV file?

5. What do the `delimiter` and `lineterminator` keyword arguments do?

6. What function takes a string of JSON data and returns a Python data structure?

7. What function takes a Python data structure and returns a string of JSON data?

## Answers

1. Excel spreadsheets can have values of data types other than strings; cells can have different fonts, sizes, or color settings; cells can have different widths and heights; can have merged cells; can have images or charts embedded in them; can have multiple worksheets; cells can have formulas.

2. You pass a File object, obtained from calling `open()`.

3. File objects for `csv.reader()` need to be opened in read mode (`'r'` or just default). File objects for `csv.writer()` need to be opened in write mode (`'w'`) with the `newline=''` keyword argument (on Windows).

4. The `writerow()` method takes a list argument and writes it as a row to the CSV file.

5. The `delimiter` keyword argument changes the character that separates cells in a row (default is comma). The `lineterminator` keyword argument changes the character that comes at the end of a row (default is newline).

6. The `json.loads()` function converts a JSON string into a Python data structure (like a dictionary or list).

7. The `json.dumps()` function converts a Python data structure into a JSON formatted string.
