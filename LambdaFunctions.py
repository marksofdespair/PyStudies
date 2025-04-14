# Regular function 

def square(x): 

    return x ** 2 

# Lambda function 

square_lambda = lambda x: x ** 2 

# Lambda functions are most commonly used as arguments to higher-order functions such as map(), filter(), and sorted(). 
# Higher-order functions are functions that can accept other functions, such as lambda functions, as arguments.

# Basic syntax
lambda [arguments]: [expression] 

# Simple Examples
# Lambda function to add two numbers 

add = lambda a, b: a + b 

print(add(3, 5))  # Output: 8 

# Lambda function to print a name 

greeting = lambda name: f"Hello, {name}!" 

print(greeting("Alice"))  # Output: Hello, Alice! 

# Using Lambda with map()
numbers = [1, 2, 3, 4, 5] 
squared = list(map(lambda x: x ** 2, numbers)) 

print(squared)  # Output: [1, 4, 9, 16, 25] 

# Using Lambda with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) 

print(even_numbers)  # Output: [2, 4, 6, 8, 10] 

# Using Lambda with sorted()
students = [('Alice', 'A', 15), ('Bob', 'B', 12), ('Charlie', 'A', 20)] 
sorted_students = sorted(students, key=lambda x: x[2]) 

print(sorted_students) 

# Output: [('Bob', 'B', 12), ('Alice', 'A', 15), ('Charlie', 'A', 20)] 

# Pros/cons
print("
Lambda functions offer several advantages:
They are concise and can make code more readable for simple operations.
They’re convenient for small, throwaway functions, especially as arguments to higher-order functions.

However, they also have limitations:

They can only contain expressions, not statements.
They are limited to a single expression, which can make complex operations difficult.
They can be harder to debug due to their anonymous nature.")
