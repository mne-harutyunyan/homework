# Use a generator expression to create a generator that yields the squares of numbers from 1 to 20.
# Iterate through this generator to print all squared values.

def generator():
    for i in range(1,21):
        result=i**2
        yield result

a=generator()
for i in range(20):
    print(next(a))


