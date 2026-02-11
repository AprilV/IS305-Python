# Chapter 5 Quick Summary - Dictionaries

**Date Completed:** January 25, 2026

## What You Learned

**Dictionaries = collections of key-value pairs**

### Core Concepts Mastered:
- Creating dictionaries: `spam = {'name': 'Zophie', 'age': 7}`
- Accessing values: `spam['name']`
- Adding/changing: `spam['color'] = 'black'`
- Getting all keys: `spam.keys()`
- Getting all values: `spam.values()`
- Getting pairs: `spam.items()`
- Checking existence: `'name' in spam`
- Safe access: `spam.get('color', 'N/A')`
- Set if missing: `spam.setdefault('age', 1)`
- Pretty printing: `pprint.pprint(spam)`

### Key Differences from Lists:
- Lists use numbers (0, 1, 2) to access items
- Dictionaries use descriptive keys ('name', 'age') to access items
- Dictionaries are unordered (order doesn't matter)

### Important Methods:
- `get()` - won't crash if key missing (returns default)
- `setdefault()` - sets value only if key doesn't exist yet
- `in` - checks if key exists
- `in spam.values()` - checks if value exists

## What to Review

**Missed Questions:**
- Empty dictionary: `{}`
- Dictionary syntax: `{'key': value}` with colon
- `'key' in spam` checks for keys
- `spam.get('key', default)` is safe way to access

## Files Created
- [Chapter_5_Summary.md](Chapter 5/Chapter_5_Summary.md) - Full reference
- [Chapter_5_Practice_Questions.md](Chapter 5/Chapter_5_Practice_Questions.md) - 8 book questions with answers

## Key Takeaway
Dictionaries let you use meaningful names instead of numbers. Much more readable for real-world data.

## Tomorrow
Chapters 6 (Strings) and 7 (Regular Expressions)
