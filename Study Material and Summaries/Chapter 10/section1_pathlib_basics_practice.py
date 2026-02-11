# SECTION 1: PATHLIB BASICS - Practice

# Q1: Import Path from pathlib module, create variable p as Path with 'folder1', 'folder2', 'folder3', print it
# Example: p = Path('spam', 'bacon', 'eggs')
# Example: print(p)



# Q2: Create variable user_path using / operator to join Path('Users') with 'Al' and 'Documents', print it
# Example: path = Path('home') / 'bob' / 'files'
# Example: print(path)
user_path = Path('Users') / 'A1' / 'Documents'



# Q3: Create variable current with current working directory, print it
# Example: current = Path.cwd()
# Example: print(current)
current = Path.cwd()
print(current)




# Q4: Create variable home with home directory, print it
# Example: home = Path.home()
# Example: print(home)
home = Path.home()
print(home)



# Q5: Create variable desktop_file as path to 'test.txt' in Desktop folder, print it
# Example: file_path = Path.home() / 'Documents' / 'report.pdf'
# Example: print(file_path)
desktop_file = Path.home() / 'Desktop' / 'test.txt'
print(desktop_file)




# Q6: Create variable p as Path with 'spam' and 'bacon', create variable p_str by converting p to string, print p and p_str
# Example: p = Path('home', 'user')
# Example: p_str = str(p)
# Example: print(p)
# Example: print(p_str)
p = Path('spam', 'bacon')
p_str = str(p)
print(p)
print(p_str)



