from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # 3 special cases
        if not prices:
            return 0
        
        if prices == sorted(prices):
            return prices[-1] - prices[0]
        
        if prices == sorted(prices, reverse=True):
            return 0
        
        sumPrice = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                sumPrice += prices[i] - prices[i-1]
        
        return sumPrice
                    