# CHAPTER 9 PRACTICE QUIZ - TEXTBOOK QUESTIONS

# Answer each question below. Your instructor will give you one question at a time.

# ==========================================
# QUESTION 1
# ==========================================
# What is the function that creates Regex objects?
# ANSWER: re.compile()



# ==========================================
# QUESTION 2
# ==========================================
# Why are raw strings often used when creating Regex objects?
# ANSWER: So backslashes are treated as literal characters and not escape sequences. 
# Without r'', you'd need to write '\\d' instead of r'\d'



# ==========================================
# QUESTION 3
# ==========================================
# What does the search() method return?
# ANSWER: A Match object (if found) or None (if not found)



# ==========================================
# QUESTION 4
# ==========================================
# How do you get the actual strings that match the pattern from a Match object?
# ANSWER: Call the .group() method on the Match object



# ==========================================
# QUESTION 5
# ==========================================
# In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?
# ANSWER: Group 0 = entire match (415-555-1234), Group 1 = first parentheses (415), Group 2 = second parentheses (555-1234)



# ==========================================
# QUESTION 6
# ==========================================
# Parentheses and periods have specific meanings in regular expression syntax. 
# How would you specify that you want a regex to match actual parentheses and period characters?
# ANSWER: Escape them with backslash: \. for period, \( and \) for parentheses



# ==========================================
# QUESTION 7
# ==========================================
# The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?
# ANSWER: If the regex has groups (parentheses), it returns tuples. If no groups, it returns strings.



# ==========================================
# QUESTION 8
# ==========================================
# What does the | character signify in regular expressions?
# ANSWER: OR - matches one pattern or another (like 'cat|dog' matches either cat or dog)



# ==========================================
# QUESTION 9
# ==========================================
# What two things does the ? character signify in regular expressions?
# ANSWER: 1) Zero or one (optional) - like (wo)? matches 'wo' or nothing. 2) Non-greedy matching when used after * or +



# ==========================================
# QUESTION 10
# ==========================================
# What is the difference between the + and * characters in regular expressions?
# ANSWER: + matches one or more (must appear at least once). * matches zero or more (can be absent)



# ==========================================
# QUESTION 11
# ==========================================
# What is the difference between {3} and {3,5} in regular expressions?
# ANSWER: {3} matches exactly 3 repetitions. {3,5} matches 3 to 5 repetitions.



# ==========================================
# QUESTION 12
# ==========================================
# What do the \d, \w, and \s shorthand character classes signify in regular expressions?
# ANSWER: \d = any digit (0-9), \w = any word character (letters, digits, underscore), \s = any whitespace



# ==========================================
# QUESTION 13
# ==========================================
# What do the \D, \W, and \S shorthand character classes signify in regular expressions?
# ANSWER: \D = any NON-digit, \W = any NON-word character, \S = any NON-whitespace (opposites of lowercase)



# ==========================================
# QUESTION 14
# ==========================================
# How do you make a regular expression case-insensitive?
# ANSWER: Pass re.IGNORECASE as second argument to re.compile()



# ==========================================
# QUESTION 15
# ==========================================
# What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?
# ANSWER: Normally matches any character EXCEPT newline. With re.DOTALL, it matches ANY character including newline.



# ==========================================
# QUESTION 16
# ==========================================
# What is the difference between .* and .*? in regular expressions?
# ANSWER: .* is greedy (matches as much as possible). .*? is non-greedy (matches as little as possible)



# ==========================================
# QUESTION 17
# ==========================================
# What is the character class syntax to match all numbers and lowercase letters?
# ANSWER: [0-9a-z] or [a-z0-9]



# ==========================================
# QUESTION 18
# ==========================================
# If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings') return?
# ANSWER: 'X drummers, X pipers, five rings' (replaces all digit sequences with X)



# ==========================================
# QUESTION 19
# ==========================================
# What does passing re.VERBOSE as the second argument to re.compile() allow you to do?
# ANSWER: Write regex with whitespace and comments for readability (whitespace is ignored)



# ==========================================
# QUESTION 20
# ==========================================
# How would you write a regex that matches a number with commas for every three digits? 
# It must match the following:
# '42'
# '1,234'
# '6,368,745'
# But not the following:
# '12,34,567' (which has only two digits between the commas)
# '1234' (which lacks commas)
# ANSWER: r'^\d{1,3}(,\d{3})*$'
# Explanation: Starts with 1-3 digits, then zero or more groups of comma+3digits, entire string must match


