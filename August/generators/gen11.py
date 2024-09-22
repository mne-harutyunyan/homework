# Write a generator function custom_reduce(func, iterable, initializer=None) that mimics the behavior
#  of functools.reduce(). It should yield intermediate results of applying func cumulatively to 
# the items of iterable, optionally starting with initializer. 
# Test this function with a list of numbers and a lambda function that adds two numbers.

def custom_reduce(func, iterable, initializer=None):
    