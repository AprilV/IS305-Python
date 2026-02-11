# Chapter 4 Quick Summary - Lists

**Date Completed:** January 25, 2026

## What You Learned

**Lists = ordered collections that can be changed**

### Core Concepts Mastered:
- Creating lists: `spam = ['cat', 'dog', 'bird']`
- Accessing items: `spam[0]` (first item), `spam[-1]` (last item)
- Slicing: `spam[1:3]` (items 1 and 2, stops before 3)
- Adding items: `append()`, `insert()`
- Removing items: `remove()`, `del`
- Finding items: `index()`, `in` operator
- Sorting: `sort()`, `reverse()`
- Looping: `for item in list:` and `enumerate()`

### Tuples (Frozen Lists):
- Use `()` instead of `[]`
- Cannot be changed after creation
- Otherwise work like lists

### Important Concept - References:
- `cheese = spam` doesn't copy the list
- Both variables point to the SAME list
- To actually copy: `import copy` then `copy.copy(spam)`

## What to Review

**Missed Questions:**
- Empty list syntax: `[]`
- Slicing stops BEFORE the second number
- List concatenation (`+`) and replication (`*`)

## Files Created
- [Chapter_4_Summary.md](Chapter 4/Chapter_4_Summary.md) - Full reference
- [Chapter_4_Practice_Questions.md](Chapter 4/Chapter_4_Practice_Questions.md) - 17 book questions with answers

## Key Takeaway
Lists use numbers to find things. Dictionaries use names (next chapter).
