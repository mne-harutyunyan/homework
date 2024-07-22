# Write a function in Python that determines whether a given number is a power of 2. 
# A number is considered a power of 2 if it can be expressed as 2^k, where k is a non-negative integer.
def pow_2(n):
    if (n <= 0):
        return False
    while (n != 1):
        if (n % 2 != 0):
            return False
        n = n // 2

    return True
print(pow_2(64))
