# CHAPTER 9 - SECTION 5: CHARACTER CLASSES - Practice

import re

# Q1: Create a regex using \d+ to match digits. Use .search() and .group() to print the digits from 'I have 42 cats'
# Example: regex = re.compile(r'\d+')
# Example: print(regex.search('There are 100 items').group())
regex = re.compile(r'\d+')
print(regex.search('I have 42 cats').group())


# Q2: Create a regex using \w+ to match words. Use .findall() to print all words in 'Hello_World 123'
# Example: regex = re.compile(r'\w+')
# Example: print(regex.findall('Python_3 rocks'))
regex = re.compile(r'\w+')
print(regex.findall('Hello_World 123'))


# Q3: Create your own character class [aeiou] to find all vowels in 'Python programming'
# Example: regex = re.compile(r'[aeiou]')
# Example: print(regex.findall('hello world'))
regex = re.compile(r'[aeiou]')
print(regex.findall('Python programming'))


# Q4: Create a negative character class [^0-9] to find all non-digits in 'abc123def'
# Example: regex = re.compile(r'[^aeiou]')
# Example: print(regex.findall('hello'))
regex = re.compile(r'[^0-9]')
print(regex.findall('abc123def'))


