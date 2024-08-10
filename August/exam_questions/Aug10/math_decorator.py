# Create a decorator that validates the input arguments of a function 
# (e.g., ensures all arguments are positive integers). Apply this decorator 
# to a function that performs mathematical operations.
def validator(function):
    def inner(*args, **kwargs):
        for i in args:
            if not isinstance(i,int):
                print("Please input an integer")
                exit()
        for i in kwargs:
            if not isinstance(kwargs[i], int):
                print("Please input an integer")
                exit()
        return function(*args,**kwargs)
    return inner
    
        
@validator
def foo(a,b):
    return f"sum is {a+b}"

print(foo(8.6,b=4))