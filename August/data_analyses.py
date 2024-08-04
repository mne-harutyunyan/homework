# Store functions for common data analysis operations (e.g., mean, median, mode, standard deviation)
#  in a dictionary. Write a function analyze_data(data, operation)
# that uses this dictionary to perform the requested analysis on a list of numbers.
def mean(args):
    return sum(args)/len(args)
def median(args):
    nums=sorted(args)
    if len(nums) % 2 != 0:
        return len(nums)//2 + 1
    else:
        return ((len(nums)/2)+ (len(nums)//2 + 1))/2
import statistics
def mode(args):
    return statistics.mode(args)
def standard_deviation(args):
    return statistics.stdev(args)

def analyze_data(data, operation):
    dict = {
        "mean":mean,
        "median":median,
        "mode":mode,
        "standard deviation":standard_deviation
    }
    res= dict.get(operation)(data)
    return res
ls=(1,2,3,4,5,6,7,8,9,6,5,5,5,5)
operation=input("Enter the operation: ")
print(analyze_data(ls,operation))