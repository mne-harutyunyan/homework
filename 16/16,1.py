# Write a recursive function to calculate the sum of all elements in a list.

def sum_ls(ls):
    if not ls:
        return 0
    return ls[0] + sum_ls(ls[1:])

ls= [1,1,1,1,1,1,1]
print(sum_ls(ls))