from typing import List
#solution1

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         size = len(nums)
#         for i in range(size):
#             if nums[i] != i:
#                 return i
#             continue
#         return i+1
# nums = [0,1]
# s =Solution()
# print(s.missingNumber(nums))

#solution2

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         st = set(nums)
#         size = len(nums)
#         for i in range(size):
#             if not i in st:
#                 return i
#             continue
#         return i+1
    
# nums = [0,1]
# s =Solution()
# print(s.missingNumber(nums))

#solution3

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        nm = sum(nums)
        size = len(nums)+1
        return sum((x for x in range(size))) - nm
nums = [0,1,2,3,5]
s =Solution()
print(s.missingNumber(nums)) 
