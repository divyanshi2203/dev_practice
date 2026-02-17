class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_val= float("inf")
        for i in range(len(prices)):
            if prices[i]<min_val:
                min_val = prices[i]
                continue
            today_profit = prices[i]-min_val
            max_profit = max(max_profit,today_profit)
        return max_profit