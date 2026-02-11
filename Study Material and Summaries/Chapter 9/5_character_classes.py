# CHAPTER 9 - SECTION 5: CHARACTER CLASSES

# What: Shorthand for common character sets
# Why: Simpler than writing [0-9] or [a-zA-Z]
# How: \d, \w, \s and their opposites

import re

# \d matches digit (0-9)
# Equivalent to [0-9]
regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
match = regex.search('My number: 415-555-4242')
print(match.group())  # 415-555-4242

# \D matches NON-digit (anything except 0-9)
regex = re.compile(r'\D+')
match = regex.findall('12 drummers, 11 pipers')
print(match)  # [' drummers, ', ' pipers']

# \w matches word character (letter, digit, underscore)
# Equivalent to [a-zA-Z0-9_]
regex = re.compile(r'\w+')
match = regex.findall('My name is Alice_123')
print(match)  # ['My', 'name', 'is', 'Alice_123']

# \W matches NON-word character (space, punctuation, etc.)
regex = re.compile(r'\W+')
match = regex.findall('My name is Alice!')
print(match)  # [' ', ' ', ' ', '!']

# \s matches whitespace (space, tab, newline)
regex = re.compile(r'\s+')
match = regex.findall('Hello   World\tPython')
print(match)  # ['   ', '\t']

# \S matches NON-whitespace
regex = re.compile(r'\S+')
match = regex.findall('Hello World Python')
print(match)  # ['Hello', 'World', 'Python']

# Making your own character class with []
# [aeiou] matches any vowel
vowel_regex = re.compile(r'[aeiouAEIOU]')
print(vowel_regex.findall('RoboCop eats baby food.'))
# ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o']

# [a-zA-Z] matches any letter
# [0-9] matches any digit
# [a-zA-Z0-9] matches letter or digit

# Negative character class with ^
# [^aeiou] matches anything EXCEPT vowels
consonant_regex = re.compile(r'[^aeiouAEIOU]')
print(consonant_regex.findall('RoboCop eats baby food.'))
# ['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.']
