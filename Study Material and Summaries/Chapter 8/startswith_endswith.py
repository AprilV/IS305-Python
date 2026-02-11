# Chapter 8 - Section 10: startswith() and endswith() Reference

# startswith() - check if string starts with something
filename = 'report.pdf'

print(filename.startswith('report'))  # True
print(filename.startswith('data'))    # False
print(filename.startswith('rep'))     # True

print()

# endswith() - check if string ends with something
print(filename.endswith('.pdf'))      # True
print(filename.endswith('.txt'))      # False
print(filename.endswith('pdf'))       # True

print()

# Case-sensitive!
url = 'https://example.com'
print(url.startswith('https'))        # True
print(url.startswith('HTTPS'))        # False

print()

# Practical use - checking file types
files = ['image.jpg', 'document.pdf', 'photo.png', 'data.csv']

for file in files:
    if file.endswith('.jpg') or file.endswith('.png'):
        print(f'{file} is an image')
    elif file.endswith('.pdf'):
        print(f'{file} is a PDF')

print()

# Multiple possible values
email = 'user@gmail.com'
print(email.endswith(('.com', '.org', '.net')))  # True (can pass tuple)
