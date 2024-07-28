
def foo(iter1, iter2):
    return iter1*iter2

def my_map(function:'function', *iterable)->list:
    ''' this function takes a function and an iterable, 
    applies the function to each item in the iterable, 
    and returns a list of the results'''
    result = []
    min_lenght = len(iterable[0])
    for item in range(len(iterable)):
        if min_lenght > len(iterable[item]):
            min_lenght = len(iterable[item])
    for i in range(min_lenght):
        current = []
        for item in iterable:
            current.append(item[i])
        result.append(function(*current))    
    return result
ls1= [1,2,3,4,5,6]
ls2= [2,3,4,5,6,22,11,3,3,56,4]
print(my_map(foo,ls1, ls2 ))

help(my_map)
    
            
    