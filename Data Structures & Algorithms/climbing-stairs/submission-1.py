class Solution:
    # time: 
    # space: 
    def climbStairs(self, n: int) -> int:

        dp = [-1 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1

        return self.recursion(n, dp)

    
    def recursion(self, n: int, dp: list) -> int:
        
        if dp[n] != -1:
            return dp[n]

        dp[n] = self.recursion(n - 1, dp) + self.recursion(n - 2, dp)
        return dp[n]