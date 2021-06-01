# Quiz description URL:
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


# Point:
# 1.Use max method.
# 2. Timeout!


# result
##!!!!!!!!!Timeout!!!!!!!!!!!!!####
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_price = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)

        return max_price

