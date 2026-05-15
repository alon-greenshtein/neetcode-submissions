class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        res = 0
        l, r = 0, 1

        while l != n and r != n:
            while prices[l] >= prices[l + 1]:
                l += 1
                if l + 1 == n:
                    return res
            
            r = l + 1
            while r != n and prices[r] >= prices[l]:
                res = max(res, prices[r] - prices[l])
                r += 1
               
            l = r
            r += 1

        return res