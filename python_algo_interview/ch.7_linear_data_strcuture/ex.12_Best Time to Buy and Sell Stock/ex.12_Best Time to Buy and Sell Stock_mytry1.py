# Quiz description URL:
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


# Point:
# 1.Brutal force.O(n^2)

# result
#!!!!!!!!!!!!!! Timeout!!!!!!!!!!!!!!!

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        # brutal force
        max_benefit = 0
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if prices[j] - prices[i] >= max_benefit:
                    max_benefit = prices[j] - prices[i]

        return max_benefit
