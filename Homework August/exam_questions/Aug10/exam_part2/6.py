# Գրել ծրագիր, որը օգտագործողից կստանա մուտքային արժեք(int) և կհաշվի արդյոք այդ թիվը պարզ է, թե՝ ոչ։

def prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(n ** 0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return f"{True}, the number is prime"
n=int(input("Enter a number:  "))
print(prime(n))

