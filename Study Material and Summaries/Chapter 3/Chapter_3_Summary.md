# Chapter 3: Functions

**Note:** This is a reference summary created for completeness. Chapter was not completed with hands-on practice.

## Table of Contents
1. [What are Functions?](#what-are-functions)
2. [def Statements](#def-statements)
3. [Parameters and Arguments](#parameters-and-arguments)
4. [Return Values](#return-values)
5. [The None Value](#the-none-value)
6. [Keyword Arguments](#keyword-arguments)
7. [Local and Global Scope](#local-and-global-scope)
8. [Exception Handling](#exception-handling)

---

## What are Functions?

Functions are reusable pieces of code that perform a specific task. You've already used built-in functions like `print()`, `len()`, `input()`.

**Why use functions?**
- Avoid repeating code
- Make code more organized
- Easier to fix bugs (fix once, works everywhere)
- Makes code more readable

---

## def Statements

Create your own functions with `def`:

```python
def hello():
    print('Hello!')
    print('How are you?')

# Call the function:
hello()
# Output:
# Hello!
# How are you?
```

**Syntax:**
- `def` keyword
- Function name
- Parentheses `()`
- Colon `:`
- Indented code block

---

## Parameters and Arguments

**Parameters** are variables in the function definition.
**Arguments** are values you pass when calling the function.

```python
def hello(name):  # 'name' is a parameter
    print(f'Hello, {name}!')

hello('Alice')  # 'Alice' is an argument
# Output: Hello, Alice!

hello('Bob')
# Output: Hello, Bob!
```

**Multiple parameters:**
```python
def add(a, b):
    print(a + b)

add(5, 3)  # Output: 8
```

---

## Return Values

Functions can return values using `return`:

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8

# Can use directly:
print(add(10, 20))  # Output: 30
```

**Key difference:**
- `print()` displays on screen
- `return` sends value back to caller (can be stored/used)

```python
def printSum(a, b):
    print(a + b)

def returnSum(a, b):
    return a + b

x = printSum(5, 3)    # Prints 8, x is None
y = returnSum(5, 3)   # Returns 8, y is 8
```

---

## The None Value

`None` represents the absence of a value.

```python
def noReturn():
    print('Hello')

result = noReturn()
print(result)  # Output: None

# Functions without 'return' automatically return None
```

**Common use:**
```python
spam = None  # Placeholder for value to be set later
```

---

## Keyword Arguments

Call functions using parameter names:

```python
def describe(name, age, city):
    print(f'{name} is {age} years old and lives in {city}')

# Positional arguments (order matters):
describe('Alice', 25, 'NYC')

# Keyword arguments (order doesn't matter):
describe(age=25, name='Alice', city='NYC')
describe(city='NYC', name='Alice', age=25)  # Same result
```

**Default values:**
```python
def greet(name, greeting='Hello'):
    print(f'{greeting}, {name}!')

greet('Alice')              # Hello, Alice! (uses default)
greet('Bob', 'Hi')          # Hi, Bob!
greet('Carol', greeting='Hey')  # Hey, Carol!
```

---

## Local and Global Scope

**Scope** determines where variables can be accessed.

### Local Scope
Variables created inside a function only exist inside that function:

```python
def spam():
    eggs = 99  # Local variable
    print(eggs)

spam()  # Output: 99
print(eggs)  # ERROR - eggs doesn't exist outside function
```

### Global Scope
Variables created outside functions are global:

```python
eggs = 42  # Global variable

def spam():
    print(eggs)  # Can read global variables

spam()  # Output: 42
print(eggs)  # Output: 42
```

### Local vs Global with Same Name
```python
eggs = 'global'

def spam():
    eggs = 'local'  # Different variable!
    print(eggs)

spam()        # Output: local
print(eggs)   # Output: global
```

### The global Statement
To modify global variables inside a function:

```python
eggs = 'global'

def spam():
    global eggs  # Declare we're using the global eggs
    eggs = 'modified'

spam()
print(eggs)  # Output: modified
```

**Rules:**
- If variable is assigned in function → local (unless declared global)
- If variable is only read → Python looks for global
- Use `global` keyword to modify global variables inside functions

---

## Exception Handling

Handle errors gracefully with try/except:

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Cannot divide by zero!')
        return None

print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Cannot divide by zero!
                      #         None
```

**Structure:**
```python
try:
    # Code that might cause an error
    risky_operation()
except ErrorType:
    # What to do if that error occurs
    handle_error()
```

**Multiple exceptions:**
```python
try:
    num = int(input('Enter number: '))
    result = 100 / num
except ValueError:
    print('That's not a number!')
except ZeroDivisionError:
    print('Cannot divide by zero!')
```

---

## Key Concepts

### Function Flow
1. Function is defined with `def`
2. Function is called by name + `()`
3. Code jumps to function definition
4. Function executes
5. `return` sends value back (or `None` if no return)
6. Code continues after function call

### When to Use Functions
- Code you'll use multiple times
- Logical grouping of related operations
- Making code more readable
- When a task can be described in one sentence

### Common Pattern
```python
def main():
    # Main program logic
    print('Program starting...')
    result = doSomething()
    print(f'Result: {result}')

def doSomething():
    # Helper function
    return 42

# Standard Python pattern:
if __name__ == '__main__':
    main()
```

---

## Summary

**Functions let you:**
- Reuse code
- Organize programs
- Pass data in (parameters/arguments)
- Get data out (return values)
- Handle errors (try/except)

**Key syntax:**
```python
def functionName(parameter1, parameter2):
    # Code block
    return value
```

**Scope rules:**
- Local variables exist only inside their function
- Global variables exist everywhere
- Use `global` keyword to modify globals inside functions

**Best practices:**
- Give functions descriptive names
- Keep functions focused on one task
- Use return values instead of print when possible
- Handle predictable errors with try/except

---

## Practice Questions (Reference Only)

1. Why are functions advantageous?
2. When does code in a function execute?
3. What statement creates a function?
4. What's the difference between a function and a function call?
5. How many global and local scopes are there?
6. What happens to local variables when function returns?
7. What is a return value?
8. What does a function return if it has no return statement?
9. How can you force a variable in a function to be global?
10. What is the data type of None?
11. What does the import areallyourpetsnamederic statement do?
12. What would you type to call a function named bacon() in the spam module after importing spam?
13. How can you prevent a program from crashing when it gets an error?
14. What goes in the try clause? What goes in the except clause?

**Note:** Since this chapter wasn't completed with hands-on practice, consider reviewing it if needed for class or projects.
