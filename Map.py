# The map() function is a built-in function in Python that applies a given function to each item in an iterable (like a list, tuple, or string) and returns a new iterable as a result.
# The basic syntax of map() is:
map(function, iterable, [iterable2, iterable3, ...]) 

def double(x): 

    return x * 2 

numbers = [1, 2, 3, 4, 5] 

doubled_numbers = map(double, numbers) 

print(list(doubled_numbers))  # Output: [2, 4, 6, 8, 10] 

# More advanced example of the use of map()
# Sample list of names
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# Using map with a lambda function to get the length of each name
name_lengths = list(map(lambda x: len(x), names))

# Using map with a defined function to capitalize each name
def capitalize_name(name):
    return name.upper()

capitalized_names = list(map(capitalize_name, names))

# Print the results
print("Original names:", names)
print("Name lengths:", name_lengths)
print("Capitalized names:", capitalized_names)

# Uncomment and modify the line below:
# your_result = list(map(lambda x: # Your function here, names))
# print("Your result:", your_result)

