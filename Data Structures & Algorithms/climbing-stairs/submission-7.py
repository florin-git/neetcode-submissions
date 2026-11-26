class Solution:
    # def climbStairs(self, n: int) -> int:
        
    #     if n <= 1:
    #         return 1

    #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # def climbStairs(self, n: int) -> int:

    #     dp = {0: 1, 1: 1}

    #     def dfs(n):
    #         if n in dp:
    #             return dp[n]

    #         res = dfs(n - 1) + dfs(n - 2)
    #         dp[n] = res
    #         return dp[n]

    #     return dfs(n)

    def climbStairs(self, n: int) -> int:

        if n <= 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


