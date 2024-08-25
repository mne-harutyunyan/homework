# Create a generator function custom_filter(func, iterable) that mimics the behavior of the built-in filter()
# function. It should yield items from iterable where func(item) returns True.
#  Test this function with a list of integers and a lambda function that checks if the number is even.

def custom_filter(function:'function', iterable):
    '''this function filter items out of an iterable based on a function
     and yields the result'''

    if function == None:
        for item in iterable:
            if item:
                yield item
    else:
        for item in iterable:
            if function(item):
                yield item
    
ls=[x for x in range(15)]
even = lambda x : x if x%2==0 else None

filterr = custom_filter(even,(ls))
for i in filterr:
    print(i)