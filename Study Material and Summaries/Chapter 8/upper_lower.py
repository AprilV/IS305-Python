# Chapter 8 - Section 8: upper() and lower() Methods Reference

text = 'Hello World'

# Convert to uppercase
print(text.upper())  # HELLO WORLD

# Convert to lowercase
print(text.lower())  # hello world

# Original string is unchanged
print(text)  # Hello World

print()  # Blank line

# Practical use - case-insensitive comparison
user_input = 'YES'

if user_input.lower() == 'yes':
    print('User said yes!')

print()  # Blank line

# Cleaning user input
name = '  ALICE  '
clean_name = name.strip().lower().capitalize()
print(clean_name)  # Alice

print()  # Blank line

# Checking passwords (case-sensitive)
password = 'MyPassword123'
print(password)  # MyPassword123 (unchanged)
print(password.lower())  # mypassword123
print(password.upper())  # MYPASSWORD123
