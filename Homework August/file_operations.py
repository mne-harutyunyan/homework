# Create a dictionary with functions for basic file operations (e.g., read, write,
# append, delete). Write a function file_manager(file_name, operation, content=None)
#  that uses this dictionary to perform the requested file operation.

def read(file_name,content=None):
    return open(file_name,mode = "r")
def write(file_name,content=""):
    res = open(file_name, mode = "w")
    res.write(content)
    return res
def append(file_name, content=" "):
    res = open(file_name, mode = "a")
    res.write(content)
    return res
def delete(file_name,content=None):
    res = open(file_name, mode = "w")
    res.write("")
    return res

def file_manager(file_name, operation, content=None):
    dict = {
        "write":write,
        "read":read,
        "append":append,
        "delete":delete
    }
    res = dict.get(operation)(file_name,content)
    return res
file_name = input("Enter files' name: ")
operation = input("Enter the operation: ")
content = None
if operation == "write":
    content = input("Enter text: ")
if operation == "append":
    content = input("Enter text: ")
file_manager(file_name,operation,content)

