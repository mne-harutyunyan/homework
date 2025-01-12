# Write a function that takes an integer n and returns a list of the first n Fibonacci numbers.
def fib(n):
    ls = []
    prev = 1
    Preprev = 0
    current = None
    for i in range(2,n):
        current = prev + Preprev
        Preprev = prev
        prev = current
        ls.append(current)
    return ls
print(fib(20))


