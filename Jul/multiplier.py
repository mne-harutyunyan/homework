# Write a function make_multiplier_of(n) that takes an integer n 
# and returns a function that multiplies its argument by n.
# Demonstrate its use with several examples.

def make_multiplier_of(n):
    def inner(x):
        return n*x
    return inner
y= make_multiplier_of(4)
print(y(y(6)))
print(y(25))

for i in range(11):
    x=make_multiplier_of(i)
    print(f"{i} * 8 = {x(8)}")

