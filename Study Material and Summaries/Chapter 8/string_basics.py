# Chapter 8 - Section 1: String Literals Practice
# Type the examples below and run this file

# Example 1: Single quotes
spam = 'Hello'
print(spam)

# Example 2: Double quotes
spam = "Hello"
print(spam)

# Example 3: Apostrophe in string (using double quotes makes it easy)
message = "Alice's cat"
print(message)

# Now try this - what happens if we use single quotes with an apostrophe?
# Uncomment the line below to test (remove the #)
# message = 'Alice's cat'  # This will cause an error!

# The fix using single quotes - escape the apostrophe with backslash
message = 'Alice\'s cat'
print(message)
