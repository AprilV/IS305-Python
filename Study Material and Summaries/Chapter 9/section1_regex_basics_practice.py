# CHAPTER 9 - SECTION 1: REGEX BASICS - Practice



# Q1: Import the re module and create a regex object that matches the pattern 'cat'
# Example: import re
# Example: dog_regex = re.compile(r'dog')
import re
cat_regex = re.compile(r'cat')



# Q2: Use the regex from Q1 to search for 'cat' in the string 'The cat sat on the mat'
# Example: match = dog_regex.search('I have a dog')
# Example: print(match.group())
match = cat_regex.search('The cat sat on the mat.')
print(match.group())


# Q3: Create a regex that matches phone numbers like 123-456-7890, search for it in 'Call 555-123-4567'
# Example: phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Example: match = phone_regex.search('My number is 415-555-1234')
# Example: print(match.group())
phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
match = phone_regex.search('555-123-4567')
print(match.group())

