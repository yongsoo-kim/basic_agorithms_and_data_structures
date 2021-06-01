# Quiz description URL:
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


# Point:
# 1.Use max method.
# 2. Use sys.maxsize


# result
# Runtime: 1120 ms, faster than 23.80% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25.2 MB, less than 50.78% of Python3 online submissions for Best Time to Buy and Sell Stock.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # profit = -sys.maxsize
        profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit

