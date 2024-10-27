from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size = len(digits)
        tmp = ""
        for i in range(size):
            tmp += str(digits[i])
        sum = int(tmp) + 1
        ls=[]
        while sum > 0:
            chlp = sum % 10
            ls.append(chlp)
            sum = sum//10
        ls.reverse()
        return ls