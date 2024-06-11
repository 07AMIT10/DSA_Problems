from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        maxP = 0
        while r<len(prices):
            if prices[l]<prices[r]:
                profit = prices[r]-prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r+=1
        return maxP
        

a = Solution()
print(a.maxProfit([1,23,34,1,45,2]))