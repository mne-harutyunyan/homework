def merge_sort(arr,l,r):
    if len(arr) < 1:
        return
    if (l < r):
        mid = (l + r) // 2
        merge_sort(arr,l,mid)
        merge_sort(arr,mid+1, r)
        merge(arr,l,mid,r)

def merge(arr,l,mid,r):
    left_part = arr[l : (mid+1)]
    right_part = arr[(mid+1): (r+1)]
    i = j= 0
    k = l 
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i+=1
        else:
            arr[k] = right_part[j]
            j+=1
        k+=1
    while i < len(left_part):
        arr[k] = left_part[i]
        i+=1
        k+=1
    while j < len(right_part):
        arr[k] = right_part[j]
        j+=1
        k+=1
        
import random, time
nums = [random.randint(0,100) for i in range(1000000)]
start = time.perf_counter()
merge_sort(nums,0,len(nums))
print(time.perf_counter() - start)

