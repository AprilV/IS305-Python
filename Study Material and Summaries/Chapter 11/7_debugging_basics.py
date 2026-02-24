# CHAPTER 11 - SECTION 7: RAISING EXCEPTIONS

# What: Raise custom exceptions with raise statement
# Why: Signal errors that your function can't handle
# How: Use raise Exception('message')

import traceback

# Raise an exception
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be single character')
    if width <= 2:
        raise Exception('Width must be greater than 2')
    if height <= 2:
        raise Exception('Height must be greater than 2')
    
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

# Handle exceptions
try:
    boxPrint('*', 4, 4)
except Exception as err:
    print('Error:', str(err))

# Get traceback as string
try:
    x = 1 / 0
except:
    errorInfo = traceback.format_exc()
    print(errorInfo)

# REMEMBER:
# - raise Exception('message') raises custom exception
# - try/except catches and handles exceptions
# - traceback.format_exc() returns error info as string
