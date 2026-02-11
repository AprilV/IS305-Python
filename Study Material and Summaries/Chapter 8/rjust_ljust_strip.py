# SECTION 12: TEXT ALIGNMENT AND WHITESPACE REMOVAL

# === TEXT ALIGNMENT ===

# rjust() - Right-align text
print('Hello'.rjust(10))           # '     Hello' (5 spaces on left)
print('Hello'.rjust(10, '*'))      # '*****Hello'
print('Hello'.rjust(20, '-'))      # '---------------Hello'

# ljust() - Left-align text
print('Hello'.ljust(10))           # 'Hello     ' (5 spaces on right)
print('Hello'.ljust(10, '*'))      # 'Hello*****'
print('Hello'.ljust(20, '-'))      # 'Hello---------------'

# center() - Center text
print('Hello'.center(10))          # '  Hello   ' (balanced spaces)
print('Hello'.center(10, '*'))     # '**Hello***'
print('Hello'.center(20, '='))     # '=======Hello========'

# Practical use: Formatting a table
print('MENU'.center(20, '='))
print('Pizza'.ljust(15) + '$12'.rjust(5))
print('Burger'.ljust(15) + '$8'.rjust(5))
print('Salad'.ljust(15) + '$6'.rjust(5))
print('=' * 20)


# === WHITESPACE REMOVAL ===

# strip() - Remove whitespace from BOTH ends
text = '   Hello World   '
print(text.strip())                # 'Hello World' (spaces removed)

user_input = '\n\n  Python  \t\n'
print(user_input.strip())          # 'Python' (all whitespace removed)

# lstrip() - Remove whitespace from LEFT end only
text = '   Hello World   '
print(text.lstrip())               # 'Hello World   ' (left spaces gone)

# rstrip() - Remove whitespace from RIGHT end only
text = '   Hello World   '
print(text.rstrip())               # '   Hello World' (right spaces gone)

# Strip specific characters (not just whitespace)
url = 'www.example.com'
print(url.strip('cmowz.'))         # 'example' (strips those chars from ends)

filename = '###report.txt###'
print(filename.strip('#'))         # 'report.txt'

# Practical use: Cleaning user input
user_name = '  Alice  '
cleaned = user_name.strip()
print(f'Welcome, {cleaned}!')      # 'Welcome, Alice!'
