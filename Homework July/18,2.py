# Create a function named get_nth_element that takes an iterable and an integer n,
# and returns the n-th element from the iterable using iter() and next().

def get_nth_element(iterable, n: "int")->int:

    a=iter(ls)
    try:
        
        while n>1 :
            next(a)
    except StopIteration:
        pass
    return ls[n]
    
ls = [1,2,3,4,5,6,7,8]
n=int(input("Enter n number: "))
print(f"the {n}th element is : {get_nth_element(ls,n)}")