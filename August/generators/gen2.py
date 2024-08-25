# Write a generator function prime_generator(n) that yields prime numbers up to n.
# Use this generator to print all prime numbers less than 100.
def prime_generator(n):
    for number in range(2, n):
        flag = True
        limit = int(number ** 0.5) + 1
        for i in range(2, limit):
            if number % i == 0:
                flag = False
                break
        if flag:
            yield number

for i in prime_generator(100):
    print(i)

        

