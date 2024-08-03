# Store functions for string manipulations (such as uppercase, lowercase, title case, and reversing a string)
# in a dictionary. Write a function manipulate_string(s, operation) that takes a string and
# an operation name, and uses the dictionary to perform the requested string manipulation.

def upper(st):
    return st.upper()
def lower(st):
    return st.lower()
def title(st):
    return st.title()
def reverse(st):
    return st[-1::-1]

def manipulate_string(s, operation):
    dict = {"uppercase": upper,"lowercase":lower,"title case":title,"reverse":reverse}
    res = dict.get(operation)(s)
    return res

s = input("Enret the string: ")
operation = input("Enret the operation: ")
print(manipulate_string(s,operation))