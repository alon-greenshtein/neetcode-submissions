class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        res = 0

        for i in range(n):
            for j in range(i+1, n):
                if (prices[j] > prices[i]):
                    res = max(res,prices[j] - prices[i])
            
        return res
        