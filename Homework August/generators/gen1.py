# Create a generator function fibonacci_generator(n) that yields the first n Fibonacci numbers.
# Test your generator by printing all numbers yielded by it.

def fibonacci_generator(n):
    previous = 1
    preprevious = 1
    for i in range(0,n):
        yield preprevious
        current = preprevious+previous
        preprevious=previous
        previous=current
        
n=int(input("Enter n: "))
if n >= 1:
    print(f"Here are the first {n} Fibonacci numbers.")
    for i in fibonacci_generator(n):
        print(i)
else:
    print('Enter only positive integers...')

