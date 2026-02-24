# SECTION 9: ASSERTIONS - Practice

# Q1: Use assert to check that variable x equals 5, with error message 'x should be 5'
# WHAT IT DOES: Checks that a condition is True, raises AssertionError if False
# ┌─ EXAMPLE ─────────────
# │ assert age >= 18, 'Must be adult'
# └───────────────────────




# Q2: Create list ages with values [10, 20, 30], use assert to check ages[0] <= ages[-1] with message 'First age should be less than or equal to last'
# WHAT IT DOES: Verifies list is sorted by comparing first and last elements  
# ┌─ EXAMPLE ─────────────
# │ numbers = [1, 2, 3]
# │ assert numbers[0] < numbers[-1], 'Not sorted'
# └───────────────────────




# Q3: Use try/except AssertionError to catch failed assertion, print error message with str(err)
# WHAT IT DOES: Handles assertion failures gracefully instead of crashing program
# ┌─ EXAMPLE ─────────────
# │ try:
# │     assert False, 'This will fail'
# │ except AssertionError as e:
# │     print(str(e))
# └───────────────────────




# Q4: Create traffic_light dict with 'ns': 'green' and 'ew': 'red', use assert to check 'red' in traffic_light.values()
# WHAT IT DOES: Ensures at least one traffic light is red (safety sanity check)
# ┌─ EXAMPLE ─────────────
# │ stoplight = {'north': 'red', 'south': 'green'}
# │ assert 'red' in stoplight.values(), 'No red light!'
# └───────────────────────




# Q5: Create function boxPrint with parameters symbol, width, height that uses assert len(symbol) == 1 with message 'Symbol must be single character'
# WHAT IT DOES: Validates function parameter meets requirement before proceeding
# ┌─ EXAMPLE ─────────────
# │ def greet(name):
# │     assert len(name) > 0, 'Name cannot be empty'
# └───────────────────────




# Q6: In boxPrint function, use assert width > 2 with message 'Width must be greater than 2'
# WHAT IT DOES: Checks that width parameter is large enough to draw a box
# ┌─ EXAMPLE ─────────────
# │ assert height > 0, 'Height must be positive'
# └───────────────────────




# Q7: In boxPrint function, use assert height > 2 with message 'Height must be greater than 2'
# WHAT IT DOES: Validates height parameter meets minimum requirements
# ┌─ EXAMPLE ─────────────
# │ assert count >= 1, 'Count must be at least 1'
# └───────────────────────




# Q8: Create list nums = [3, 1, 4, 2], use assert to check nums[0] <= nums[-1], demonstrate assertion failure
# WHAT IT DOES: Shows how assertion catches incorrect assumptions about data
# ┌─ EXAMPLE ─────────────
# │ values = [5, 2]
# │ assert values[0] < values[1], 'Not ascending'
# └───────────────────────
