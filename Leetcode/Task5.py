from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        max_val = max(nums)
        ls = [0] * (max_val + 1)

        for i in range(len(nums)):
            for j in range(len(ls)):
                if nums[i] == j:
                    ls[j]+=1
        nums = []
        for i in range(len(ls)):
            while ls[i] > 0:
                nums.append(i)
                ls[i] -= 1
        return nums


nums  = [2,0,1]
s = Solution()
print(s.sortColors(nums))
