# Write a function that takes three numbers as input and returns the maximum of the three.

def max(x,y,z):
    max = x
    if (y >= x) and (y >= z):
        max = y
    if (z >= x) and (z >= y):
        max = z
    
    return max
print(max(int(input("enter first number: ")), int(input("enter second number: ")), int(input("enter third number: "))))