# Implement a generator function custom_range(start, end, step) that mimics Python’s built-in range() 
# function but can accept a float step. Use this generator to print numbers from 0 to 5 with a step of 0.5.

def custom_range(start, end, step):
    result = start 
    while result != end:
        result += step
        yield result
        
for i in custom_range(0,5,0.5):
    print(i)