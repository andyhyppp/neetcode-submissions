class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        p = prices[0]
        for i in range(1, len(prices)):
            ans = max(ans, (prices[i] - p))
            p = min(prices[i], p)
        
        return ans