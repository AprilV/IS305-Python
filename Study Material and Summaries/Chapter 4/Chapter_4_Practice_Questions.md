# Chapter 4 Practice Questions
## From "Automate the Boring Stuff with Python" - End of Chapter Questions

---

## PRACTICE QUESTIONS (From the book)

**1. What is `[]`?**

**2. How would you assign the value `'hello'` as the third value in a list stored in a variable named `spam`? (Assume `spam` contains `[2, 4, 6, 8, 10]`.)**

For the following three questions, let's say `spam` contains the list `['a', 'b', 'c', 'd']`.

**3. What does `spam[int(int('3' * 2) // 11)]` evaluate to?**

**4. What does `spam[-1]` evaluate to?**

**5. What does `spam[:2]` evaluate to?**

For the following three questions, let's say `bacon` contains the list `[3.14, 'cat', 11, 'cat', True]`.

**6. What does `bacon.index('cat')` evaluate to?**

**7. What does `bacon.append(99)` make the list value in `bacon` look like?**

**8. What does `bacon.remove('cat')` make the list value in `bacon` look like?**

**9. What are the operators for list concatenation and list replication?**

**10. What is the difference between the `append()` and `insert()` list methods?**

**11. What are two ways to remove values from a list?**

**12. Name a few ways that list values are similar to string values.**

**13. What is the difference between lists and tuples?**

**14. How do you type the tuple value that has just the integer value `42` in it?**

**15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?**

**16. Variables that "contain" list values don't actually contain lists directly. What do they contain instead?**

**17. What is the difference between `copy.copy()` and `copy.deepcopy()`?**

---

## ANSWER KEY

**1.** `[]` is an empty list (a list with no values).

**2.** `spam[2] = 'hello'` (Remember: lists are zero-indexed, so the third value is at index 2)

**3.** `'d'`  
Explanation: `'3' * 2` = `'33'`, then `int('33')` = `33`, then `33 // 11` = `3`, then `spam[3]` = `'d'`

**4.** `'d'` (The last item in the list)

**5.** `['a', 'b']` (A slice from index 0 up to but not including index 2)

**6.** `1` (The index of the first occurrence of `'cat'`)

**7.** `[3.14, 'cat', 11, 'cat', True, 99]` (`append()` adds to the end)

**8.** `[3.14, 11, 'cat', True]` (`remove()` removes the first occurrence of `'cat'`)

**9.** 
- Concatenation: `+` operator
- Replication: `*` operator

**10.** 
- `append()` adds a value to the END of a list
- `insert()` adds a value at a SPECIFIC index position

**11.** 
- The `del` statement: `del spam[2]`
- The `remove()` method: `spam.remove('cat')`

**12.** Both:
- Can be indexed and sliced
- Can be used in `for` loops
- Can be used with `len()`
- Can use `in` and `not in` operators
- Can be concatenated with `+` and replicated with `*`

**13.** 
- Lists are MUTABLE (can be changed)
- Tuples are IMMUTABLE (cannot be changed)
- Lists use square brackets `[]`, tuples use parentheses `()`

**14.** `(42,)` - You need a trailing comma to distinguish it from just a value in parentheses

**15.** 
- List to tuple: `tuple(['cat', 'dog'])`
- Tuple to list: `list(('cat', 'dog'))`

**16.** Variables contain REFERENCES to lists (memory addresses), not the actual list values themselves.

**17.** 
- `copy.copy()` creates a SHALLOW copy (copies the list but not nested lists inside)
- `copy.deepcopy()` creates a DEEP copy (copies the list AND any lists inside it)

---

## HANDS-ON PRACTICE EXERCISES

Try these coding exercises to reinforce your learning:

### Exercise 1: Basic List Operations
```python
# Create a list of your top 5 favorite foods
# Print the first and last items
# Add a new food to the end
# Remove the second item
# Print the final list
```

### Exercise 2: List Slicing
```python
# Create a list of numbers from 0 to 9
# Use slicing to get the first half
# Use slicing to get the last 3 numbers
# Use slicing to get every other number
```

### Exercise 3: The Comma Code
Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with `and` inserted before the last item.

For example, passing the list `['apples', 'bananas', 'tofu', 'cats']` to the function would return `'apples, bananas, tofu, and cats'`.

### Exercise 4: Coin Flip Streaks
For this exercise, we'll try doing an experiment. If you flip a coin 100 times and write down an "H" for each heads and "T" for each tails, you'll create a list that looks like `['T', 'T', 'T', 'T', 'H', 'T']`.

If you asked a human to make up 100 random coin flips, you'll probably end up with alternating head-tail results like `['H', 'T', 'H', 'T', 'H', 'H', 'T', 'H']`, which looks random but isn't mathematically random. A human will have a hard time writing down a streak of six heads or six tails in a row, even though it is highly likely to happen in truly random coin flips.

Write a program to find out how often a streak of six heads or six tails comes up in a randomly generated list of heads and tails. Your program should:
1. Create a list of 100 'heads' or 'tails' values
2. Check if there is a streak of 6 heads or 6 tails
3. Repeat this experiment 10,000 times
4. Calculate what percentage of experiments had a streak

Hint: Use `random.randint(0, 1)` to generate random 0s and 1s.

### Exercise 5: Character Picture Grid
Write a program that uses a list of lists to represent a grid and prints it out.

```python
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
```

The program should print the image when run, like this:
```
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
```

Hint: You'll need to use a loop within a loop and access items with `grid[x][y]`.

---

## KEY TAKEAWAYS FROM CHAPTER 4

✓ Lists are ordered, mutable sequences of values  
✓ Access values with indexes (starting at 0) and slices  
✓ Modify lists with methods like `append()`, `insert()`, `remove()`, `sort()`  
✓ Use `in` and `not in` to check for values  
✓ Variables store references to lists, not the lists themselves  
✓ Use `copy.copy()` or `copy.deepcopy()` to make actual copies  
✓ Tuples are like immutable lists - can't be changed after creation  

---
