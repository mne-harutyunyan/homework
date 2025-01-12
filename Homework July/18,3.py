# Create a function named apply_function that takes an iterable and a function,
# and applies the function to each element of the iterable,
# returning a list of the results.
def foo(iterable):
    ls = []
    for item in range(len(iterable)):
        ls.append(iterable[item])
    return ls

def apply_function(func, iterable):
    a=func(iterable)
    return a

listi=[45,56,56]
print(apply_function(foo, listi))