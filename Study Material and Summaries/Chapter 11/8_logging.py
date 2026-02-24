# CHAPTER 11 - SECTION 8: LOGGING MODULE

# What: Log messages for debugging instead of print()
# Why: Easy to enable/disable, shows timestamps and levels
# How: Use logging.basicConfig() then logging.debug/info/warning/error/critical

import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, 
                   format=' %(asctime)s - %(levelname)s - %(message)s')

# Use logging in a function
def factorial(n):
    logging.debug(f'Start of factorial({n})')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug(f'i={i}, total={total}')
    logging.debug(f'End of factorial({n})')
    return total

logging.debug('Start of program')
result = factorial(5)
logging.debug('End of program')

# Five logging levels
logging.debug('Detailed diagnostic info')
logging.info('General info, things working')
logging.warning('Unexpected, but not error')
logging.error('Something failed')
logging.critical('Fatal error')

# Disable all logging
logging.disable(logging.CRITICAL)

# REMEMBER:
# - logging.basicConfig() configures format and level
# - Five levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
# - logging.disable() turns off all logging
# - Log to file: logging.basicConfig(filename='log.txt')
