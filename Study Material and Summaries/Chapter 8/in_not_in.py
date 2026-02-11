# Chapter 8 - Section 6: in and not in Operators Reference

# The 'in' operator - check if substring exists
text = 'Hello World'

print('Hello' in text)        # True
print('Goodbye' in text)      # False
print('World' in text)        # True
print('world' in text)        # False (case-sensitive!)

print()  # Blank line

# The 'not in' operator - check if substring does NOT exist
print('Goodbye' not in text)  # True (Goodbye is NOT in text)
print('Hello' not in text)    # False (Hello IS in text)

print()  # Blank line

# Practical use - validating user input
user_input = 'yes'
if 'y' in user_input.lower():
    print('User said yes!')

# Checking for specific words
message = 'The cat sat on the mat'
if 'cat' in message:
    print('Message mentions a cat')

if 'dog' not in message:
    print('Message does not mention a dog')
