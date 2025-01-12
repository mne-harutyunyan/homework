# Create a generator function repeat_element(element, times) that yields the given element a specified 
# number of times. Test this generator with different inputs.

def repeat_element(element, times):
    for i in range(times):
        yield element

for i in repeat_element("hello",5):
    print(i)

for i in repeat_element("barev",10):
    print(i)


