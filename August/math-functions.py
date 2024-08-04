# Create a dictionary with various math functions (e.g., square, cube, square root, factorial). 
# Write a function math_operations(number, operation) that uses this 
# dictionary to apply the requested math function to a number.
def square(x):
    return x**2
def cube(x):
    return x**3
def square_root(x):
    return x**0.5
def factorial(x):
    return 1 if x<1 else x * factorial(x-1)

def math_operations(number, operation):
    dict = {
        "square":square,
        "cube":cube,
        "square root":square_root,
        "factorial":factorial
    }
    res = dict.get(operation)(number)
    return res

num = int(input("Enter a number: "))
operation = input("Enter the operation: ")

print(math_operations(num,operation))

