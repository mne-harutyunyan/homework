# Store functions for common list transformations (e.g., sorting, reversing, filtering, mapping)
#  in a dictionary. Write a function transform_list(lst, operation) that uses
# this dictionary to perform the requested transformation on a list.
def sort(ls):
    ls.sort()
    return ls
def reverse(ls):
    res = []
    for i in range(len(ls)):
        res.insert(0,ls[i])
    return res
def filter(ls):
    res = []
    for i in range(len(ls)):
        if ls[i]>10:
            res.append(ls[i])
    return res
def map(ls):
    res = [x*2 for x in ls]
    return res

def transform_list(lst, operation):
    dict = {
        "sort":sort,
        "reverse": reverse,
        "filter":filter,
        "map":map
    }
    res = dict.get(operation)(lst)
    return res
lst = [1,789,3,55,76,3,4,5,6,0,4,2,456]
operation = input("Enter the operation: ")
print(transform_list(lst,operation))