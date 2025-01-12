# Write a function that takes an integer as input and returns True if the number is prime, False otherwise.

def prime(n):
    if n > 0:   
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
    return False
   
print(prime(int((input("Enter a number: ")))))
