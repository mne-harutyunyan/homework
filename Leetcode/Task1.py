from typing import List
# time complexity n**2 , solution1


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         size = len(nums)
#         for i in range(size):
#             for j in range(1,size):
#                 if nums[i] + nums[j] == target and i != j:
#                     return i, j

#solution2
         
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         size = len(nums)
#         st = {}
#         for i in range(size):
#             dif = target - nums[i]
#             if nums[i] in st:
#                 return[st[nums[i]], i]
#             else:
#                 st[dif] = i


#solution3

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        st = set(nums)
        for i in range(1,size):
            x = nums[i]
            if (target - x) in st and not (i == nums.index(target-x)):
                return i, nums.index(target-x)           