# Develop a function called my_zip that combines elements from multiple iterables
#  into tuples,similar to the built-in zip() function, and returns a list of these tuples.
# Requirements:
# The function should stop zipping when the shortest iterable is exhausted 
# and return a list of tuples.
# Include type annotations and a detailed docstring.
# # Do not use the built-in zip() in your code.
 

def my_zip(*iterables):
    min_lenght = len(iterables[0])
    for item in range(len(iterables)):
        if min_lenght > len(iterables[item]):
            min_lenght = len(iterables[item])
    res = []
    for i in range(min_lenght):
        tp=tuple([iterable[i] for iterable in iterables])
        res.append(tp)
    return res

ls1=[1,2,3,4]
ls2=[5,3,4,5,6,7]
ls3=['hello','bye',"Bob"]
print(my_zip(ls1,ls2,ls3))