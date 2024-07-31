# Create a function make_counter() that returns a function 
# that,when called, increments and returns a counter variable.
# The counter should start at 0 and increment by 1 each time the function is called.
def make_counter():
    count = 0
    def inner():
        nonlocal count;
        count+=1
        print(count)
    return inner

x=make_counter()
x()
x()

y=make_counter()
y()
y()
y()
# print(hex(id(3)))
# print(y.__closure__)



