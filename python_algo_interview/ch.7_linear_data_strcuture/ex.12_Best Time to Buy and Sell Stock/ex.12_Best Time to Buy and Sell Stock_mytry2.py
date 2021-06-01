# Quiz description URL:
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


# Point:
# 1.Set minimum price as price[0]
# 2.Find min_price while traversing the list.


# result
# Runtime: 944 ms, faster than 87.60% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25 MB, less than 95.06% of Python3 online submissions for Best Time to Buy and Sell Stock.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        min_price = prices[0]
        max_price = 0

        for i in range(1, n):
            if min_price >= prices[i]:
                min_price = prices[i]
                continue

            if max_price <= prices[i] - min_price:
                max_price = prices[i] - min_price

        return max_price
