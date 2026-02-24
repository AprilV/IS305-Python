# SECTION 8: LOGGING MODULE - Practice

# Q1: Import logging module
# WHAT IT DOES: Makes logging functions available for debugging and tracking program execution
# ┌─ EXAMPLE ─────────────
# │ import sys
# └───────────────────────




# Q2: Use logging.basicConfig() with level=logging.DEBUG and format=' %(asctime)s - %(levelname)s - %(message)s'
# WHAT IT DOES: Configures logging to show timestamp, level, and message for all debug messages and above
# ┌─ EXAMPLE ─────────────
# │ logging.basicConfig(level=logging.INFO, format='%(message)s')
# └───────────────────────




# Q3: Use logging.debug() to log message 'Start of program'
# WHAT IT DOES: Writes a debug-level message for detailed diagnostic information
# ┌─ EXAMPLE ─────────────
# │ logging.debug('Entering function')
# └───────────────────────




# Q4: Use logging.info() to log message 'Program is running normally'
# WHAT IT DOES: Records informational message confirming things are working as expected
# ┌─ EXAMPLE ─────────────
# │ logging.info('File loaded successfully')
# └───────────────────────




# Q5: Use logging.warning() to log message 'Low disk space'
# WHAT IT DOES: Logs a warning about something unexpected but not an error
# ┌─ EXAMPLE ─────────────
# │ logging.warning('Connection slow')
# └───────────────────────




# Q6: Use logging.error() to log message 'Failed to save file'
# WHAT IT DOES: Records that a serious error occurred and something failed
# ┌─ EXAMPLE ─────────────
# │ logging.error('Database connection failed')
# └───────────────────────




# Q7: Use logging.critical() to log message 'System out of memory'
# WHAT IT DOES: Logs a critical error that may cause program to crash
# ┌─ EXAMPLE ─────────────
# │ logging.critical('Server unreachable')
# └───────────────────────




# Q8: Use logging.disable(logging.CRITICAL) to disable all logging
# WHAT IT DOES: Turns off all logging messages at or below CRITICAL level
# ┌─ EXAMPLE ─────────────
# │ logging.disable(logging.WARNING)
# └───────────────────────




# Q9: Create function factorial that takes n, uses logging.debug() to log 'Start of factorial(n)', returns n factorial
# WHAT IT DOES: Logs entry point of function for debugging execution flow
# ┌─ EXAMPLE ─────────────
# │ def calculate(x):
# │     logging.debug(f'Calculating with x={x}')
# │     return x * 2
# └───────────────────────




# Q10: In factorial function, use for loop with range(1, n + 1) and use logging.debug() to log i value each iteration
# WHAT IT DOES: Tracks loop progress by logging each iteration's value
# ┌─ EXAMPLE ─────────────
# │ for num in range(5):
# │     logging.debug(f'Processing {num}')
# └───────────────────────




# Q11: Use logging.basicConfig() with filename='mylog.txt' to log to file instead of screen
# WHAT IT DOES: Redirects all logging output to a file for permanent record
# ┌─ EXAMPLE ─────────────
# │ logging.basicConfig(filename='app.log', level=logging.DEBUG)
# └───────────────────────
