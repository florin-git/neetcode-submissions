class Solution:
    # # time: O(2^n)
    # # space: O(n)
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     def dfs(i):
    #         if i >= len(cost):
    #             return 0
            
    #         return cost[i] + min(dfs(i + 1), dfs(i + 2))

    #     return min(dfs(0), dfs(1)) # starting from 0 or 1

    # time: O(n)
    # space: O(n)
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [-1 for _ in range(len(cost) + 1)]
        dp[len(cost)] = 0

        def dfs(i):
            if i >= len(cost):
                return 0

            if dp[i] != -1:
                return dp[i]
            
            dp[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return dp[i]

        return min(dfs(0), dfs(1)) # starting from 0 or 1
        


