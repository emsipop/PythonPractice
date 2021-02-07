# Helper function that takes in an int value and returns a value
def fix_three(n):
    if n >= 20 and n <= 29: # If the value is between 20 and 29, then the value stays the same
        return n
    elif n % 3 == 0: # If the value is a multiple of three, then the value becomes 0
        return 0
    else:
        return n

# Funuction which take three integer values a b c as arguments
def no_three_sum(a, b, c):
    return fix_three(a) + fix_three(b) + fix_three(c) # Uses the helper function to return the sum of the values following the rule
