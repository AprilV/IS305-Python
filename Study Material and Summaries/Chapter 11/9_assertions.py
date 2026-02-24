# CHAPTER 11 - SECTION 9: ASSERTIONS

# What: Sanity checks with assert statement
# Why: Catch programmer errors early (not user input errors)
# How: assert condition, 'error message'

# Basic assertion
ages = [15, 22, 26, 47, 54, 57, 73, 80, 92]
assert ages[0] <= ages[-1], 'First age should be <= last'
print('List is sorted')

# Assertion that fails
nums = [5, 3, 9, 1]  # Not sorted
try:
    assert nums[0] <= nums[-1], 'Not sorted'
except AssertionError as e:
    print(f'Assertion failed: {e}')

# Traffic light example - catch bugs
def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    
    # Sanity check: at least one light must be red
    assert 'red' in stoplight.values(), 'Neither light is red!'

traffic = {'ns': 'green', 'ew': 'red'}
switchLights(traffic)
print(f'Traffic lights: {traffic}')

# REMEMBER:
# - assert checks if condition is True
# - Raises AssertionError if False
# - Use for programmer errors, not user input validation
# - Disabled with: python -O script.py
