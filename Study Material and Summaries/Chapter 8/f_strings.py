# Chapter 8 - Section 7: F-Strings Reference

# Basic f-string - insert variable into string
name = 'Alice'
age = 25

print(f'My name is {name} and I am {age} years old.')

print()  # Blank line

# F-strings with expressions
width = 10
height = 5

print(f'The area is {width * height}')

print()  # Blank line

# F-strings with multiple variables
first = 'Bob'
last = 'Smith'
year = 2026

print(f'{first} {last} was born in {year - 25}')

print()  # Blank line

# Useful for formatting output
price = 19.99
quantity = 3

print(f'Total cost: ${price * quantity}')
print(f'Item: ${price} x {quantity} = ${price * quantity}')
