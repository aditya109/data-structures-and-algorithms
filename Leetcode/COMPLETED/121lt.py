from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 999999999

        max_profit = 0
        length = len(prices)
        for i in range(length):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i]-min_price > max_profit:
                max_profit = prices[i]-min_price
        return max_profit
print(Solution().maxProfit([7,6,4,3,1]))