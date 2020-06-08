"""Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0."""

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy, buy_in = -1, False
        sell, sell_out = -1, False

        idx = 0
        profit = 0

        while idx != len(prices): 
            current_price = prices[idx]
           
            if not buy_in and not sell_out:
                # if i have not bought anything,
                # then obviously i would have not sold anything
                if buy == -1 or buy > current_price:
                    # have not bought anything yet or current_price is better (less) than previous buy
                    buy = current_price 
                elif buy < current_price:
                    # found a greater price => ready to BUY IN
                    buy_in = True
            
            if buy_in and not sell_out:
                # if i would have bought something
                # then and only then i have to sell something
                if sell == -1 or sell < current_price:
                    # haven't sold anything yet or current_price is better (more) than previous sell
                    sell = current_price
                if sell > current_price or idx == len(prices) -1:
                    # found a lesser price => ready to SELL OUT
                    sell_out = True

            if buy_in and sell_out:
                profit += sell-buy
                print(f"profit = {profit}")
                
                idx-=1
                # Transaction is complete
                buy, sell = -1, -1
                buy_in, sell_out = False, False
            idx+=1

        return profit