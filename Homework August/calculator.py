# Create a dictionary-based calculator where each arithmetic operation (addition,
# subtraction, multiplication, division) is a function stored in a dictionary.
# Write a function calculate(operand1, operand2, operator) 
# that uses this dictionary to perform the requested operation.

def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    return x / y if y!=0 else print("division by zero isn't possible")
def calculate(operand1, operand2, operator):
    dict = {"+" : add, "-" : sub, "*" : mul, "/": div}
    if dict.get(operator):
        res=dict.get(operator)(operand1,operand2)
    return res

operation = input("Enter operation: ")
x = int(input("Enter x: "))
y = int(input("Enter y: "))

print(f"Result is: {calculate(x,y, operation)}")