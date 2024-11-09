import timeit
def BubbleSort(ls):
    size=len(ls)  # 1 milisecond + 3 milisecond
    for i in range(size-1): # n-1 milisecond
        for j in range(size-1-i): # n-1-i milisecond
            if ls[j]>ls[j+1]: # 2 milisecond
                ls[j],ls[j+1]=ls[j+1],ls[j] # 2 milisecond
    return ls
ls = [-76,67,43,2,1,6,-9,5,-7,3,0] # 1 milisecond
print(BubbleSort(ls)) # 1 milisecond
#time complexity is O(n**2)



def SelectionSort(ls):
    size = len(ls) # 1 milisecond + 3 milisecond
    for i in range(size): # n milisecond
        min = i # 1 milisecond
        for j in range(i + 1, size): # n+1 milisecond
            if ls[j] < ls[min]: # 2 milisecond
                min = j # 1 milisecond
        ls[i], ls[min] = ls[min], ls[i] # 2 milisecond
    return ls
print(SelectionSort(ls)) # 1 milisecond
#time complexity is O(n**2)
h = SelectionSort(ls)
b = BubbleSort(ls)

h1=timeit.timeit(lambda : h, number = 1000000)
b1=timeit.timeit(lambda : b, number = 1000000)
print(h1>b1)