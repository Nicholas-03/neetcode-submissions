class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            if (minPrice > prices[i - 1]):
                minPrice = prices[i - 1]
            if maxProfit < prices[i] - minPrice:
                maxProfit = prices[i] - minPrice

        return maxProfit