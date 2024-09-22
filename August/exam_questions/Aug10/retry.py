# Create a decorator that adds retry logic to a function. The decorator should retry
# the function a specified number of times if it raises an exception. 
# Apply this decorator to a function thatreads data from a file.
import time
def retry(limit=3):
    def delay(delay=1):
        def decorator(func):
            def wrapper(*args,**kwargs):
                for i in range(limit):
                    try:
                        return func(*args,**kwargs)
                    except Exception as e:
                        print(f"function can't be executed {i+1} time, trying to execute in {delay} seconds.")
                        time.sleep(delay)
                print("Function can't be executed anymore")
            return wrapper
        return decorator
    return delay
1
@retry(4)(2)
def read(file_name):
    fs = open(file_name)
    return fs.read()

read("new_outpu.txt")
