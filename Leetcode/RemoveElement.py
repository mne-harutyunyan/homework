def removeElement(self, nums: list[int], val: int) -> int:
    j = 1
    for i in range(0,len(nums)):
        if nums[i] != val:
            nums[j-1] = nums[i]
            j+=1
    return j-1