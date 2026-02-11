# SECTION 3: CHECKING PATHS - Practice

# Q1: Import Path from pathlib module, create win_dir Path for C:/Windows, check if exists, print result
# Example: win_dir = Path('C:/Program Files')
# Example: print(win_dir.exists())



# Q2: Check if win_dir is a directory, print result
# Example: print(win_dir.is_dir())
print(win_dir.is_dir())



# Q3: Create test_file Path for 'test.txt' in home directory, check if exists, print result
# Example: test_file = Path.home() / 'data.txt'
# Example: print(test_file.exists())
test_file = Path.home() / 'test.txt'
print(test_file.exists())



# Q4: Create variable cwd_path with Path.cwd(), check if absolute path, print result
# Example: print(Path.cwd().is_absolute())
cwd_path = Path.cwd()
print(Path.cwd().is_absolute())



# Q5: Create rel_path Path for 'spam/eggs', check if absolute, print result
# Example: rel_path = Path('data/files')
# Example: print(rel_path.is_absolute())
rel_path = Path('spam/eggs')
print(rel_path.is_absolute())



# Q6: Create doc_path Path for 'documents/file.txt', create variable abs_doc by converting doc_path to absolute using .absolute(), print doc_path and abs_doc
# Example: my_path = Path('data/report.txt')
# Example: absolute_path = my_path.absolute()
# Example: print(my_path, absolute_path)
doc_path = Path('documents/file.txt')
abs_doc = doc_path.absolute()
print(doc_path, abs_doc)



# Q7: Create calc_path Path for C:/Windows/System32/calc.exe, check if file using .is_file(), check if directory using .is_dir(), print both results
# Example: program_path = Path('C:/Windows/notepad.exe')
# Example: print(program_path.is_file())
# Example: print(program_path.is_dir())
calc_path = Path('C:/Windows/System32/calc.exe')
print(calc_path.is_file())
print(calc_path.is_dir())


