# Implement an infinite generator function infinite_sequence() that yields numbers starting from 1 and 
# increments by 1 indefinitely. Use next() to retrieve and print the first 10 numbers from this generator.
def infinite_sequence():
    n=1
    while n>=1:
        yield n
        n+=1

a = infinite_sequence()
for i in range(10):
    print(next(a))

print(infinite_sequence())
print(a)