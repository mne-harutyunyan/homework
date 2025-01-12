# Write a recursive function to check if a list is sorted in ascending order.
def asc(ls):
    if len(ls) <= 1:
        return True
    if ls[0] <= ls[1]:
        return asc(ls[1:])
    else:
        return False

ls= [2,3]
print(asc(ls))