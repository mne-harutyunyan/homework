# Create a dictionary with functions to calculate the area of different geometric shapes 
# (circle, square, rectangle, triangle). Write a function calculate_area(shape, **kwargs)
# that uses this dictionary to calculate the area based on the provided shape and parameters.
def circle(r):
    pi = 3.14
    return pi*r**2
def square(x):
    return x**2
def rectangle(a,b):
    return a*b
def triangle(a,b):
    return (a*b)/2

def calculate_area(shape, **kwargs):
    dict = {"circle": circle, "square": square,"rectangle": rectangle,"triangle": triangle}
    res = dict[shape](**kwargs)
    return  res
shape = input("Enter the shape: ")
if shape == "circle":
    r = int(input("enter r: "))
    print(f"the area of {shape} is {calculate_area(shape, r=r)}.")
elif shape == "square":
    x = int(input("enter x: "))
    print(f"the area of {shape} is {calculate_area(shape, x=x)}.")
elif shape == "rectangle":
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    print(f"the area of {shape} is {calculate_area(shape, a = a, b=b)}.")
elif shape == "triangle":
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    print(f"the area of {shape} is {calculate_area(shape, a = a, b=b)}.")

