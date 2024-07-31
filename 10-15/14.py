#task1

#n = int(input("Enter n number: "))
#def foo():
#    for i in range(n, -1, -1):
#        print(i)
#foo()

#task2

#n = int(input("Enter n number: "))
#def foo():
#    for i in range(0,n+1):
#        print(i)
#foo()

#task3

#def foo():
#    ls = [1,2,3,4]
#    for i in range(len(ls)):
#        print(ls[i])
#foo()

#task4
#def foo():
#    m = 0
#    n = int(input("please enter a number: "))
#    nm = str(n)
#    for i in nm:
#        m = m + int(i)
#    print(m)
#foo() 

#task5
#def foo():
#    str = input("enter any string: ")
#    for i in str:
#        if i == i.upper():
#            print(i)
#            break
#foo()

#task6
def foo():
    ls = [1,2,3,78,5,6,7]
    maxi = ls[0]
    for i in range(len(ls)):
        if maxi < ls[i]:
            maxi = ls[i]
    minimum = ls[0]
    for i in range(len(ls)):
        if minimum > ls[i]:
            minimum = ls[i]
    print(f"minimum element is {minimum}")
    print(f"maximum element is {maxi}")
foo()
