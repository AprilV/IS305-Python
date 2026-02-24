# SECTION 7: RAISING EXCEPTIONS AND TRACEBACK - Practice

# Q1: Use raise to raise an Exception with message 'This is an error message'
# WHAT IT DOES: Creates and raises a custom exception that stops program execution
# ┌─ EXAMPLE ─────────────
# │ raise Exception('Something went wrong')
# └───────────────────────




# Q2: Use raise Exception() to raise an exception if variable x is less than 0, with message 'x cannot be negative'
# WHAT IT DOES: Validates input and raises exception when condition is not met
# ┌─ EXAMPLE ─────────────
# │ if age < 18:
# │     raise Exception('Must be 18 or older')
# └───────────────────────




# Q3: Use try/except to attempt to divide 10 by 0, and use except Exception as err to catch the error and print str(err)
# WHAT IT DOES: Catches division by zero error and handles it gracefully instead of crashing
# ┌─ EXAMPLE ─────────────
# │ try:
# │     result = 5 / 0
# │ except Exception as err:
# │     print('Error:', str(err))
# └───────────────────────




# Q4: Import traceback module
# WHAT IT DOES: Provides functions for working with error traceback information
# ┌─ EXAMPLE ─────────────
# │ import sys
# └───────────────────────




# Q5: Use try/except to catch an error from 1/0, then use traceback.format_exc() to get error info as string and print it
# WHAT IT DOES: Captures complete error traceback as a string for logging or saving to file
# ┌─ EXAMPLE ─────────────
# │ try:
# │     x = 10 / 0
# │ except:
# │     error_info = traceback.format_exc()
# │     print(error_info)
# └───────────────────────




# Q6: Use try/except to catch error, use open() to create 'errorlog.txt' in write mode, use write() to write traceback.format_exc() to file
# WHAT IT DOES: Saves error information to a file for later review instead of just printing
# ┌─ EXAMPLE ─────────────
# │ try:
# │     bad_code()
# │ except:
# │     f = open('error.txt', 'w')
# │     f.write(traceback.format_exc())
# │     f.close()
# └───────────────────────




# Q7: Create function boxPrint that takes symbol, width, height parameters and uses raise Exception() if len(symbol) != 1
# WHAT IT DOES: Validates that symbol parameter is exactly one character before proceeding
# ┌─ EXAMPLE ─────────────
# │ def checkAge(age):
# │     if age < 0:
# │         raise Exception('Age cannot be negative')
# └───────────────────────




# Q8: In boxPrint function, use raise Exception() if width is less than or equal to 2 with message 'Width must be greater than 2'
# WHAT IT DOES: Ensures width parameter meets minimum requirements before drawing box
# ┌─ EXAMPLE ─────────────
# │ if temperature < -273.15:
# │     raise Exception('Below absolute zero')
# └───────────────────────
