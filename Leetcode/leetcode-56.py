# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices):
        l = 0
        r = 0
        maxProfit = 0

        while l < len(prices):
            while r < len(prices) and prices[r] - prices[l] >= 0:
                maxProfit = max(maxProfit, prices[r] - prices[l])
                r += 1

            l = r

        return maxProfit


prices = [7,6,4,3,1]
print(Solution().maxProfit(prices))