# Use a generator expression to filter and yield only even numbers from a list of numbers.
#  Test this generator with a list of integers from 1 to 50.

ls=[x for x in range(1,51)]

# def generator(ls):
#     for i in range(len(ls)):
#         if i % 2 != 0:
#             yield i

# gen = generator(ls)
# for i in gen:
#     print(i)

a = (x for x in ls if x%2==0)
for i in a:
    print(i)