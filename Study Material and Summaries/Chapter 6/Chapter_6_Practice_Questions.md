# Chapter 6 Practice Questions - Manipulating Strings

**Date Completed:** January 26, 2026

---

## Question 1
**Q:** What are escape characters?

**Your Answer:** Not sure initially, then confirmed: `\n` is an escape character

**Correct Answer:** Escape characters are special characters that start with a backslash `\` that let you include things in strings that would otherwise be hard to type, like newlines, tabs, or quotes within quotes.

**Examples:**
- `\n` = newline
- `\t` = tab
- `\'` = single quote
- `\"` = double quote
- `\\` = backslash

**Status:** ✅ Correct (after clarification)

---

## Question 2
**Q:** What do the `\n` and `\t` escape characters represent?

**Your Answer:** `\n` takes you down to the next line, `\t` is tab for indentation

**Correct Answer:** 
- `\n` = newline (moves to next line)
- `\t` = tab (indentation)

**Status:** ✅ Correct

---

## Question 3
**Q:** How can you put a `\` backslash character in a string?

**Your Answer:** (Uncertain)

**Correct Answer:** Use `\\` (double backslash) or use a raw string with `r` prefix:
- `print('C:\\Users')` → `C:\Users`
- `print(r'C:\Users')` → `C:\Users`

The first backslash escapes the second one, producing a single backslash in the output.

**Status:** ⚠️ Review needed

---

## Question 4
**Q:** The string value `"Howl's Moving Castle"` is a valid string. Why isn't it a problem that the single quote character in the word `Howl's` isn't escaped?

**Your Answer:** Because you used double quotes instead of single quotes in the string

**Correct Answer:** The string uses **double quotes** to start and end, so the single quote (apostrophe) inside is just a regular character. If you used single quotes to delimit the string, you'd need to escape it: `'Howl\'s Moving Castle'`

**Status:** ✅ Correct

---

## Question 5
**Q:** If you don't want to put `\n` in your string, how can you write a string with newlines in it?

**Your Answer:** Use triple quotes `'''...'''`

**Correct Answer:** Use triple quotes (`'''` or `"""`) to create a multiline string:
```python
print('''Hello
World''')
```

**Status:** ✅ Correct

---

## Question 6
**Q:** What do the following expressions evaluate to?
```python
'Hello world!'[1]
'Hello world!'[0:5]
'Hello world!'[:5]
'Hello world!'[3:]
```

**Your Answer:** 
- First one: `'e'` ✓
- Others: explained after reviewing

**Correct Answer:**
1. `'Hello world!'[1]` = `'e'` (second character, index 1)
2. `'Hello world!'[0:5]` = `'Hello'` (indices 0,1,2,3,4)
3. `'Hello world!'[:5]` = `'Hello'` (same as above, starts from beginning)
4. `'Hello world!'[3:]` = `'lo world!'` (from index 3 to end)

**Key Point:** Slicing `[start:stop]` goes up to but NOT including stop.

**Status:** ✅ Correct

---

## Question 7
**Q:** What do the following expressions evaluate to?
```python
'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()
```

**Your Answer:** Initially thought `.isupper()` counted uppercase letters

**Correct Answer:**
1. `'Hello'.upper()` = `'HELLO'` (converts to all uppercase)
2. `'Hello'.upper().isupper()` = `True` (checks if all uppercase - returns True/False, not a count)
3. `'Hello'.upper().lower()` = `'hello'` (first uppercase, then lowercase)

**Key Point:** `.isupper()` is a CHECK (returns True/False), not a count.

**Status:** ⚠️ Review: Remember `.isupper()` returns True/False, not a count

---

## Question 8
**Q:** What do the following expressions evaluate to?
```python
'Remember, remember, the fifth of November.'.split()
'-'.join('There can be only one.'.split())
```

**Your Answer:** Initially thought they were connected; understood after explanation

**Correct Answer:**
1. `'Remember, remember, the fifth of November.'.split()` = `['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']` (list of words)
2. `'-'.join('There can be only one.'.split())` = `'There-can-be-only-one.'` (spaces replaced with dashes)

**Breakdown of #2:**
- `'There can be only one.'.split()` → `['There', 'can', 'be', 'only', 'one.']`
- `'-'.join([...])` → joins with dashes between each word

**Key Point:** Split returns a LIST. Join takes a list and creates a STRING.

**Status:** ⚠️ Marked as wrong - Review: split/join pattern

---

## Question 9
**Q:** What string methods can you use to right-justify, left-justify, and center a string?

**Your Answer:** `.rjust()`, `.ljust()`, `.center()`

**Correct Answer:**
- `.rjust(n)` - right justify
- `.ljust(n)` - left justify
- `.center(n)` - center

Where `n` is the total width of the resulting string.

**Status:** ✅ Correct

---

## Question 10
**Q:** How can you trim whitespace characters from the beginning or end of a string?

**Your Answer:** `.rstrip()`, `.lstrip()`, `.strip()`

**Correct Answer:**
- `.strip()` - removes whitespace from both sides
- `.lstrip()` - removes whitespace from left (beginning)
- `.rstrip()` - removes whitespace from right (end)

**Remember:** 
- `lstrip()` = remove from LEFT
- `rstrip()` = remove from RIGHT  
- `strip()` = remove from BOTH

**Status:** ✅ Correct

---

## Summary

**Total Questions:** 10

**Correct:** 7
- Questions 1, 2, 4, 5, 6, 9, 10

**Need Review:** 3
- Question 3: How to include literal backslash (`\\` or raw string `r'...'`)
- Question 7: `.isupper()` returns True/False (not a count)
- Question 8: Split/join pattern - split creates list, join creates string

---

## Topics to Review

### 1. Escape Characters for Literal Backslashes
To get a literal `\` in your string:
- Use `\\` (double backslash): `'C:\\Users'`
- Or use raw string: `r'C:\Users'`

**Why?** Single `\` is used for escape sequences, so to get an actual backslash, you need to escape it with another backslash.

### 2. String Testing Methods Return Boolean
Methods like `.isupper()`, `.islower()`, `.isalpha()`, `.isdigit()`, `.isalnum()` return **True or False**, NOT counts or numbers.

```python
'HELLO'.isupper()  # Returns: True (not "5" for 5 uppercase letters)
'hello'.islower()  # Returns: True (not "5" for 5 lowercase letters)
```

### 3. Split and Join Pattern
Common pattern for replacing characters:
```python
# Replace spaces with dashes:
'-'.join('hello world'.split())  # 'hello-world'

# How it works:
# Step 1: 'hello world'.split() → ['hello', 'world']
# Step 2: '-'.join([...]) → 'hello-world'
```

**Key points:**
- `split()` converts string → list
- `join()` converts list → string
- Whatever is before `.join()` goes BETWEEN each list item

---

## Key Concepts Mastered

✅ Escape characters (`\n`, `\t`, `\'`, etc.)
✅ String indexing and slicing
✅ Case conversion (`.upper()`, `.lower()`)
✅ String testing (`.startswith()`, `.endswith()`)
✅ Text alignment (`.rjust()`, `.ljust()`, `.center()`)
✅ Removing whitespace (`.strip()`, `.lstrip()`, `.rstrip()`)
✅ Triple quotes for multiline strings
✅ Quote mixing (single vs double quotes)

## What to Practice More

1. **Backslash escaping** - When do you need `\\` vs when can you use raw strings?
2. **Boolean return values** - Remember validation methods return True/False
3. **Chaining methods** - Understanding `'Hello'.upper().lower()` flow
4. **Split/join combinations** - Using them together to transform strings

---

## Overall Performance

**Great job!** You got 7 out of 10 correct on the first try. The three areas to review are common gotchas:
- Escaping backslashes is tricky (that's why raw strings exist!)
- Forgetting that `is___()` methods return booleans is common
- Split/join can be confusing at first, but it's a powerful pattern

Keep the summary file handy for reference - you don't need to memorize everything, just remember these tools exist!
