# Chapter 7 Summary - Pattern Matching with Regular Expressions

**Date Completed:** January 27, 2026

## What You Learned Today

### Core Concept
Regular expressions (regex) are powerful patterns for finding and matching text. Instead of searching for exact strings, you can search for patterns like "any phone number" or "any email address."

### Essential Functions & Methods
1. **`import re`** - Import the regex module
2. **`re.compile(r'pattern')`** - Create a regex object
3. **`.search(text)`** - Find first match, returns Match object
4. **`.group()`** - Extract the matched string from Match object
5. **`.findall(text)`** - Find all matches, returns list
6. **`.sub('replacement', text)`** - Replace matches with new text

### Key Operators Covered

**Quantifiers (How Many):**
- `?` = optional (0 or 1 time)
- `*` = zero or more times
- `+` = one or more times
- `{n}` = exactly n times
- `{n,m}` = between n and m times

**Character Classes (What to Match):**
- `\d` = digit
- `\w` = word character  
- `\s` = whitespace
- `\D`, `\W`, `\S` = NOT digit/word/whitespace
- `.` = any character (wildcard)

**Special Operators:**
- `|` = OR (match this OR that)
- `( )` = groups (extract parts of the match)
- `\` = escape special characters

**Matching Behavior:**
- Greedy (`.*`) = match as much as possible
- Non-greedy (`.*?`) = match as little as possible
- Case-insensitive = use `re.IGNORECASE` flag

## Practical Examples You Ran

### Phone Number Matching
```python
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneRegex.search('My number is 415-555-1234')
mo.group()   # '415-555-1234'
mo.group(1)  # '415'
mo.group(2)  # '555-1234'
```

### OR Matching (Pipe)
```python
batRegex = re.compile(r'Bat(man|mobile|copter)')
batRegex.search('Batmobile lost a wheel').group()  # 'Batmobile'
```

### Optional Matching
```python
batRegex = re.compile(r'Bat(wo)?man')
batRegex.search('Batman').group()    # 'Batman'
batRegex.search('Batwoman').group()  # 'Batwoman'
```

### Zero or More vs One or More
```python
# * matches zero or more
re.compile(r'Bat(wo)*man').search('Batman').group()  # 'Batman'

# + requires at least one
re.compile(r'Bat(wo)+man').search('Batman')  # None (no match)
```

### Find All Matches
```python
phoneRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
phoneRegex.findall('Call 415-555-1234 or 212-555-0000')
# Returns: ['415-555-1234', '212-555-0000']
```

### Substitution (Replace)
```python
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave documents to Agent Bob.')
# Returns: 'CENSORED gave documents to CENSORED.'
```

### Character Classes
```python
# \d for digits
re.compile(r'\d\d\d-\d\d\d-\d\d\d\d').search('415-555-1234').group()

# \w for word characters
re.compile(r'\w+').search('Hello there!').group()  # 'Hello'

# Custom classes
re.compile(r'[a-zA-Z]+').search('123abc456').group()  # 'abc'
```

### Greedy vs Non-Greedy
```python
# Greedy - matches the whole thing
re.compile(r'<.*>').search('<a> <b>').group()  # '<a> <b>'

# Non-greedy - stops at first match
re.compile(r'<.*?>').search('<a> <b>').group()  # '<a>'
```

## Files Created
1. **regex_examples.py** - All code examples with comments
2. **Regex_Cheat_Sheet.md** - Quick reference for all operators
3. **Chapter_7_Practice_Exercises.md** - 20 practice questions with answers
4. **Chapter_7_Summary.md** - This file

## Practice Questions Progress
- **Completed:** 7 out of 20 questions attempted
- **Got Right:** Questions 4, 13
- **Need Review:** Questions 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15
- **Remaining:** Questions 16-20 filled in for reference

## Key Takeaways

### What You Can Do Now
✅ Understand what regex patterns do when you see them in code
✅ Use basic regex for phone numbers, emails, etc.
✅ Know the difference between `.search()` and `.findall()`
✅ Understand groups and how to extract parts of matches
✅ Use character classes like `\d`, `\w`, `\s`

### What You Don't Need to Memorize
- Every single operator and symbol
- Complex regex patterns from memory
- Exact syntax for every feature

### How to Use Regex in Real Life
1. **Google it:** "regex phone number python"
2. **Copy pattern:** Most patterns already exist online
3. **Test it:** Use regex101.com to test patterns
4. **Refer to cheat sheet:** Use your Regex_Cheat_Sheet.md
5. **Read and understand:** When you see regex in code, you can figure out what it does

## What's Next
- **Later:** Review the practice questions when fresh
- **PowerShell Project:** Upcoming (50% of grade)
- **Study Approach:** You have all reference materials - use them!

## Important Reminder
You said: "When you throw the code in front of me I can figure out what it's doing"

**That's EXACTLY what you need!** You don't need to write regex from scratch - you need to:
- Understand patterns when you see them ✓
- Know where to look for patterns (Google, cheat sheet) ✓
- Be able to modify existing patterns ✓

You've accomplished all of this today. Great work!

---

**Time Investment:** Several hours
**Chapters Completed This Week:** 4, 5, 6, 7
**Status:** Chapter 7 COMPLETE ✅
