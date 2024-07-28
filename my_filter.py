def foo(a):
    if a > 10:
        return a

def my_filter(function:'function', iterable)->list:
    '''this function filter items out of an iterable based on a function
     and return a list of the filtered items'''
    result = []
    if function == None:
        for item in iterable:
            if item:
                result.append(item)
    else:
        for item in iterable:
            if function(item):
                result.append(item)
    return f"This is the filtered items {result}"
print(my_filter(None,(1,2,3,4,0,0,0,98,76,54,0,0,-1)))
print(my_filter(foo,(1,2,3,4,98,76,54)))
# help(my_filter)

