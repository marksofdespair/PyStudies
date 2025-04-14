# There are two types of Functions in Py.
# User Defined Functions and Built-in Functions

# Examples of Built-in Functions:
print()
str(object)
len()
help()

# Example 1
print(str(int(3.14))) # Output of 3

# Example 2
destination_name = "Venkatanarasimharajuvaripeta"

# Built-in function: len()
length_of_destination = len(destination_name)

# Built-in function: print()
print(length_of_destination)

# Example 3
help("string")

# Output
NAME
    string - A collection of string constants.

MODULE REFERENCE
    https://docs.python.org/3.8/library/string
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.
.....

# EXERCISE
tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Code:

# Checkpoint 1
max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price)

# Checkpoint 2
min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price)

# Checkpoint 3
rounded_price = round(tshirt_price, 1)
print(rounded_price)
