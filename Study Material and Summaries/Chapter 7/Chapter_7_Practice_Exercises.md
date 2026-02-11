# Chapter 7 Practice Exercises - Pattern Matching with Regular Expressions

Answer the following questions. Type your answers below each question.



## 1. What is the function that creates Regex objects?

**Your answer:** import regex

**Correct answer:** re.compile()

**Note:** You import the module with `import re`, but the function that creates Regex objects is `re.compile()`


import re

## 2. Why are raw strings often used when creating Regex objects?

**Your answer:** So that's going to be the slash R. I'm guessing because strings are easier to work with

**Correct answer:** Raw strings (the `r` prefix) prevent Python from interpreting backslashes as escape sequences. This allows you to write `\d`, `\w`, `\s` directly instead of having to double them as `\\d`, `\\w`, `\\s`. Since regex patterns use many backslashes, raw strings make them cleaner and easier to read.


---

## 3. What does the search() method return?

**Your answer:** Well the search method will return whatever it's searching for

**Correct answer:** A Match object (or None if no match is found). You then use `.group()` on the Match object to get the actual string that was matched.


---

## 4. How do you get the actual strings that match the pattern from a Match object?

**Your answer:** use group()

**Correct!** ✓


---

## 5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?

**Your answer:** Group 0 would be the area code, group 1 would be the next three numbers, and group 2 would be the last four digits

**Correct answer:** 
- Group 0: The entire match (415-555-1234) - group 0 is always the full match
- Group 1: 415 (first parentheses group - area code)
- Group 2: 555-1234 (second parentheses group - includes the dash!)


---

## 6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?

**Your answer:** regex.compile(r\('.'))

**Correct answer:** Use a backslash `\` to escape them: `\(` for left paren, `\)` for right paren, `\.` for period.
Example: `re.compile(r'\(Hello\)')` matches "(Hello)"


---

## 7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?

**Your answer:** I think if it returns a tuple it's not using a group

**Correct answer:** It's the opposite! 
- No groups (no parentheses) → returns list of strings
- Has groups (parentheses) → returns list of tuples


---

## 8. What does the | character signify in regular expressions?

**Your answer:** It splits two expressions

**Correct answer:** OR - matches either the pattern on the left OR the pattern on the right.
Example: `r'Batman|Tina Fey'` matches "Batman" OR "Tina Fey"


---

## 9. What two things does the ? character signify in regular expressions?

**Your answer:** I don't remember

**Correct answer:** 
1. Optional matching - match 0 or 1 time (e.g., `(wo)?`)
2. Non-greedy matching - when after * or +, matches as little as possible (e.g., `.*?`)


---

## 10. What is the difference between the + and * characters in regular expressions?

**Your answer:** The plus symbol is non greedy and the * is greedy

**Correct answer:** 
- `*` = matches zero or more times (can match zero occurrences)
- `+` = matches one or more times (must match at least one occurrence)


---

## 11. What does {3} do in a regular expression?

**Your answer:** 3rd group

**Correct answer:** Matches exactly 3 repetitions of the preceding pattern.
Example: `(Ha){3}` matches "HaHaHa" (exactly three "Ha"s)


---

## 12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?

**Your answer:** \w is looking for a word, \d is going to delete something, \s is whitespace

**Correct answer:**
- `\d` = any digit (0-9)
- `\w` = any word character (letters, digits, underscore)
- `\s` = any whitespace (space, tab, newline)


---

## 13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?

**Your answer:** \D is not digits, \W is not words or letters, \S is not whitespace

**Correct!** ✓


---

## 14. How do you make a regular expression case-insensitive?

**Your answer:** .upper.lower

**Correct answer:** Pass `re.IGNORECASE` (or `re.I`) as the second argument to `re.compile()`
Example: `re.compile(r'robocop', re.IGNORECASE)`


---

## 15. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?

**Your answer:** I don't remember

**Correct answer:** 
- Normally: `.` matches any character except newline
- With `re.DOTALL`: `.` matches any character including newline


---

## 16. What is the difference between .* and .*?

**Correct answer:** (Question likely meant `.*` vs `.*?`)
- `.*` = greedy - matches as much as possible
- `.*?` = non-greedy - matches as little as possible


---

## 17. What is the character class syntax to match all numbers and lowercase letters?

**Correct answer:** `[0-9a-z]` or `[a-z0-9]`


---

## 18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?

**Correct answer:** `'X drummers, X pipers, five rings, X hens'`
(Replaces all digit sequences with 'X')


---

## 19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?

**Correct answer:** Allows you to add whitespace and comments inside the regex pattern to make it more readable. Whitespace is ignored.


---

## 20. How would you write a regex that matches a number with commas for every three digits? It must match the following:
- '42'
- '1,234'
- '6,368,745'

But not the following:
- '12,34,567' (which has only two digits between the commas)
- '1234' (which lacks commas)

**Correct answer:** `r'^\d{1,3}(,\d{3})*$'`
Explanation: 1-3 digits at start, then zero or more groups of (comma + exactly 3 digits)


---
