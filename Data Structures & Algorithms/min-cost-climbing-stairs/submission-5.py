class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # dp = {}
        # def dfs(i):
        #     if i >= len(cost):
        #         return 0

        #     if i in dp:
        #         return dp[i]

        #     dp[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
        #     return dp[i]

        # return min(dfs(0), dfs(1))


        dp = [0] * (len(cost) + 2)
        # dp[0] = cost[0]
        # dp[1] = cost[1]

        for i in range(len(cost) - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])

        return min(dp[0], dp[1])

