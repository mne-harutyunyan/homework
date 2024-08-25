# Create a generator exception_propagator(iterable) that yields each item in iterable. 
# If an item is "error", raise a ValueError exception with the message “An error occurred!“. 
# Test this generator with a list containing the string "error".

def exception_propagator(iterable):
    for i in range(len(iterable)):

        if iterable[i].upper() == "ERROR":
            raise ValueError('An error occurred!')
        else:
            yield iterable[i]

ls=["hello","Bob",'error', 'hi']
generator = exception_propagator(ls)
for i in generator:
    print(i)
                             
