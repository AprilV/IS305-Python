# CHAPTER 9 - SECTION 3: REPETITION - Practice

import re

# Q1: Create a regex that matches 'Batman' or 'Batwoman' (wo is optional), test with both
# Example: regex = re.compile(r'Super(wo)?man')
# Example: print(regex.search('Superman').group())

regex = re.compile(r'Bat(wo)?man')
print(regex.search('Batman').group())

# Q2: Create a regex that matches 'Ha' repeated exactly 3 times, test with 'HaHaHa'
# Example: regex = re.compile(r'(Ho){2}')
# Example: print(regex.search('HoHo').group())
regex = re.compile(r'(Ha){3}')
print(regex.search('HaHaHa').group())


# Q3: Create a regex that matches one or more digits, test with 'My age is 25'
# Example: regex = re.compile(r'\d+')
# Example: print(regex.search('I have 5 cats').group())
regex = re.compile(r'\d+')
print(regex.search('My age is 25').group())

