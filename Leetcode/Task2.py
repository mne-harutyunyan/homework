from typing import List
#solution1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            cell = prices[i]
            if cell - buy < 0:
                buy = cell
            elif cell - buy > max_profit:
                max_profit = cell-buy
        return max_profit
    
prices = [7,1,5,3,6,4] 
s=Solution()
print(s.maxProfit(prices))   