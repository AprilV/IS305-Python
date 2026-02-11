# Chapter 8 - Section 9: isX() Methods Reference

# isalpha() - True if only letters (no spaces, numbers, symbols)
print('hello'.isalpha())    # True
print('hello123'.isalpha()) # False
print('hello world'.isalpha()) # False (space!)

print()

# isdigit() - True if only digits
print('123'.isdigit())      # True
print('123abc'.isdigit())   # False
print('12.5'.isdigit())     # False (decimal point!)

print()

# isalnum() - True if only letters AND/OR numbers (no spaces/symbols)
print('hello123'.isalnum()) # True
print('hello'.isalnum())    # True
print('123'.isalnum())      # True
print('hello 123'.isalnum()) # False (space!)

print()

# isspace() - True if only whitespace (spaces, tabs, newlines)
print('   '.isspace())      # True
print('hello'.isspace())    # False

print()

# isupper() - True if all letters are uppercase (ignores numbers/symbols)
print('HELLO'.isupper())    # True
print('HELLO123'.isupper()) # True
print('Hello'.isupper())    # False

print()

# islower() - True if all letters are lowercase (ignores numbers/symbols)
print('hello'.islower())    # True
print('hello123'.islower()) # True
print('Hello'.islower())    # False

print()

# Practical use - validating input
username = 'alice123'
password = '12345'

if username.isalnum():
    print('Valid username')

if password.isdigit():
    print('Password is all numbers (weak!)')
