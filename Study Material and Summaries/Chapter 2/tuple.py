# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    """Return a tuple of strings"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    
    # Construct a tuple with shout1 and shout2: shout_words
    # Tuples use parentheses and commas: (item1, item2)
    shout_words = (shout1, shout2) 

    # Return shout_words back to the caller
    return shout_words

# Call shout_all() and unpack the returned tuple into yell1 and yell2
# yell1 gets the first element, yell2 gets the second element
yell1, yell2 = shout_all('congratulations', 'you')

# Print yell1 and yell2
print(yell1)  # Outputs: congratulations!!!
print(yell2)  # Outputs: you!!!