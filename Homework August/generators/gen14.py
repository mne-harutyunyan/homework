# Implement a generator function custom_map(func, iterable) that mimics the behavior of the built-in map()
#  function. It should apply func to each item in iterable and yield the results one by one.
#  Test your function with a sample list and a lambda function that squares each element.


def custom_map(function, *iterable):

    min_lenght = len(iterable[0])
    for item in range(len(iterable)):
        if min_lenght > len(iterable[item]):
            min_lenght = len(iterable[item])
    for i in range(min_lenght):
        current = []
        for item in iterable:
            current.append(item[i])
        yield function(*current)    

list = [x for x in range(1,15)]
square = lambda x : x**2
generator= custom_map(square,list)
for i in generator:
    print(i)