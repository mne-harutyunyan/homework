# Create two generators: gen1() yields numbers from 1 to 5, and gen2() uses yield from to yield
#  all values from gen1() and then yields numbers from 6 to 10. Print all values yielded by gen2().
def gen1(n):
    x=1
    while x!=n+1:
        yield x
        x+=1 

def gen2(start, end):       
    generator1 = gen1(5)
    for i in generator1:
        yield i
    
    while start!=end+1:
        yield start
        start+=1 


generator2 = gen2(6,10)
for i in generator2:
    print(i)