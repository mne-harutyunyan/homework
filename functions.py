#task 1: Create a lambda function that returns another lambda function 
# which multiplies its argument by a given factor.
 
# a=lambda x : lambda : x * 8
# print(a(8)())

#task 2: Write a function make_adder(n) that returns a function
#  that adds n to its argument.

# def make_adder(n):
#     def inner(x):
#         return x + n
#     return inner
# adder = make_adder(6)
# # print(adder(5))

#task 3: Create a function apply_twice(f, x) that applies a given 
# function f to an argument x two times.
# def f(x):
#     return x*25

# def apply_twice(f : callable, x):
#     a = f(x)
#     b = f(x)
#     return f"this is the first time: {a}\nthis is the second time: {b}"
# a = int(input("Enter x number: "))
# apply = apply_twice(f,a)
# print(apply)

#task 4: Write a function compose(f, g) that returns a new function 
# which is the composition of the functions f and g.

# def f(x):
#     return x+1
# def g(y):
#     return y+1

# def compose(f, g):
#     def inner(x,y):
#         return f(x) + g(y)
#     return inner

# comp = compose(f,g)
# x=int(input("Enter x number: "))
# y=int(input("Enter y number: "))
# print(f"sum of the numbers following {x} and {y} is : {comp(x,y)}")

#task 5: Implement a function power_factory(n) that returns a function 
# which raises its argument to the power of n.

# def power_factory(n):
#     def inner(x):
#         return x**n
#     return inner
# x = int(input("Enter x number: "))
# n = int(input("Enter n number: "))
# pow = power_factory(n)
# print(f"{x} to the power of {n} is {pow(x)}")

#task 6: Use the map function with a lambda to square all elements in a list.

# def my_map(function:'function', *iterable)->list:
#     ''' this function takes a function and an iterable, 
#     applies the function to each item in the iterable, 
#     and returns a list of the results'''
#     result = []
#     min_lenght = len(iterable[0])
#     for item in range(len(iterable)):
#         if min_lenght > len(iterable[item]):
#             min_lenght = len(iterable[item])
#     for i in range(min_lenght):
#         current = []
#         for item in iterable:
#             current.append(item[i])
#         result.append(function(*current))    
#     return result

# numbers = [1, 2, 3, 4, 5]
# square = lambda x: x ** 2
# res = my_map(square, numbers)
# print(res)

#task 7: Use the filter function with a lambda 
# to filter out all even numbers from a list.

# ls = [1,2,3,4,5,6]
# even_numbers = lambda x : x if x % 2 != 0 else False
# print(list(filter(even_numbers, ls)))

#task 8: Implement a function make_greeting(greeting) 
# that takes a greeting string and returns a function
# that takes a name and prints the greeting followed by the name.

# def make_greeting(greeting):
#     greet = greeting
#     def inner(name):
#         return f"{greeting}, dear {name}."
#     return inner
# greet = input("Enter greeting text: ")
# name = input("Enter your name: ")
# greeting = make_greeting(greet)
# print(greeting(name))

#task 9: Write a function make_accumulator(start=0) that returns a function
# which adds its argument to start and returns the new total each time it is called.
# def make_accumulator(start=0):
#     start = start
#     def inner():
#         nonlocal start;
#         start+=1
#         return start
#     return inner
# acc = make_accumulator(8)

# print(acc())
# print(acc())
# print(acc())

#task 10: Implement a function make_config(key, value) that returns a function 
# which, when called, returns a dictionary with the given key-value pair.
# def make_config(key, value):
#     def inner():
#         dict = {key : value}
#         return dict
#     return inner
# result = make_config("name", "Bob")
# print(result())

#task 11: Write a function make_logger(level) that returns a function
# which logs messages with the specified log level.
# def make_logger(level):
#     level = level
#     def inner():
#         dict = {
#     "ERROR": "This is an error message",
#     "WARNING": "This is a warning",
#     "INFO": "This is an info message",
#     }
#         if level == dict.keys():
#             pass
#         return dict[level]
#     return inner
# message1 = input("Enter level: ")
# message=message1.upper()
# log = make_logger(message)
# print(log())
