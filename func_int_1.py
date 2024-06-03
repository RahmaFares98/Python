import random

def randInt(min=None, max=None):
    # Ensure max is a non-negative integer, if provided
    if max is not None and max < 0:
        raise ValueError("max must be a non-negative integer")
    
    # Ensure min is not greater than max, if both are provided
    if min is not None and max is not None and min > max:
        raise ValueError("min cannot be greater than max")
    
    # Default behavior if no arguments are provided
    if min is None and max is None:
        return random.randint(0, 100)
    
    # If only max is provided, set min to 0
    if min is None:
        return random.randint(0, max)
    
    # If only min is provided, set max to 100
    if max is None:
        return random.randint(min, 100)
    
    # If both min and max are provided, use them
    return random.randint(min, max)

print(randInt())                 # Should print a random number between 0 and 100
print(randInt(max=50))           # Should print a random number between 0 and 50
print(randInt(min=50))           # Should print a random number between 50 and 100
print(randInt(min=20, max=30))   # Should print a random number between 20 and 30

try:
    print(randInt(min=30, max=20))  # Should raise an error
except ValueError as e:
    print(e)
try:
    print(randInt(max=-10))         # Should raise an error
except ValueError as e:
    print(e)
