#task1
def foo(x):
    if x<0:
        return
    foo(x-1)
#    print(x)

x=5
foo(x)

#task2
def boo(y):
    if y<0:
        return
#    print(y)
    boo(y-1)
y=5
boo(y)

#task3
def doo(z):
    if z<=1:
        return 1
    return z * doo(z-1)
z=6
#print(doo(z))


#task4
def goo(n):
    if n<=1:
        return 1
    return n + goo(n-1)
# n=4
#print(goo(n))


#task5

def loo(ls):
    if not ls:
        return     
    # print(ls[0])
    loo(ls[1:])

ls = [1,2,3,"hello",'world']
loo(ls)

#task6

def yoo(ls):
    if not ls:
        return 0
    return 1 + yoo(ls[1:])

ls = ['hello','world',16,56,"python", 3,14]
# print(yoo(ls))


# #task7

def moo(st):
    if not st:
        return 
    moo(st[1:]) 
    # print(st[0],end=" ")
st="hello"
moo(st)

#task8

def fib(n):
    if n in (1,2):
        return 1
    return fib(n-2) + fib(n-1)
n=10
# print(fib(n))
    
#task9

def noo(s1):
    if not s1:
        return
    # print(s1[0])
    noo(s1[1:])
s1="Python"
noo(s1)

#task10
def polindrome(s3):
    if len(s3) in (0,1):
        return True
    if s3[0]!=s3[-1]:
        return False
    polindrome(s3[1:-1])
    return True
s3="radar"
# print(polindrome(s3))
 

#task11

def sum(num):
    if num < 10:
        return num
    return num%10 + sum(num//10)
num=1237

print(sum(num))