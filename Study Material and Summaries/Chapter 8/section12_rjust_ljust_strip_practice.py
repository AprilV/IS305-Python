# SECTION 12: TEXT ALIGNMENT AND WHITESPACE REMOVAL - Practice

# Q1: Create variable 'word' with value 'Python', right-align it in a field of width 15
# Example: name = 'Bob'
# Example: print(name.rjust(10))
word = 'Python' 
print(word.rjust(15))


# Q2: Create variable 'title' with value 'MENU', center it in a field of width 20 with dashes as fill character
# Example: header = 'INFO'
# Example: print(header.center(12, '*'))
title = 'MENU'
print(title.center(20, '-'))


# Q3: Create variable 'item' with value 'Pizza', left-align it in a field of width 15
# Example: product = 'Book'
# Example: print(product.ljust(10))
item = 'Pizza'
print(item.ljust(15))


# Q4: Create variable 'text' with value '   hello world   ' (spaces on both ends), remove all whitespace from both ends
# Example: data = '  test  '
# Example: print(data.strip())
text = '   hello world   '
print(text.strip())



# Q5: Create variable 'filename' with value '***photo.jpg***', remove all asterisks from both ends
# Example: path = '###file.txt###'
# Example: print(path.strip('#'))
filename = '***photo.jpg***'
print(filename.strip('*'))

