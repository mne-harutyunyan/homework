# Write a Python script that manually iterates over a list of numbers 
# using the iter() and next() functions. 
# This task will help you understand how Python handles iteration behind the scenes.

ls=[1,2,3,3,4,5,6,7]
a=iter(ls)
try:
    while ls:
        print(next(a),end=" ")
except StopIteration:
    pass