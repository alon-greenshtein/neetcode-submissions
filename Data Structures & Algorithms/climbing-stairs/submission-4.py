class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {1: 1, 2: 2}
        def f(n):
            if n not in dp:
                dp[n] = f(n - 1) + f(n - 2)
            return dp[n]
        
        return f(n)