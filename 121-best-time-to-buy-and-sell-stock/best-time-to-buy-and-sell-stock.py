class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_e = prices[0]
        for p in prices:
            max_profit = max(max_profit, p - min_e)
            min_e = min(p, min_e)
        return max_profit
                