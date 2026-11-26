class Solution:
    # # time: O(n * 2^a)
    # # space: O(t)
    # def change(self, amount: int, coins: List[int]) -> int:
        
    #     def dfs(i, a):

    #         if a == 0:
    #             return 1

    #         if i == len(coins):
    #             return 0

    #         res = dfs(i + 1, a)

    #         if a - coins[i] >= 0:
    #             res += dfs(i, a - coins[i]) 
            
    #         return res

    #     return dfs(0, amount)

    # time: O(n * 2^a)
    # space: O(t)
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]

        
        def dfs(i, a):

            if a == 0:
                return 1

            if i == len(coins):
                return 0

            if dp[i][a] != -1:
                return dp[i][a]

            dp[i][a] = dfs(i + 1, a)

            if a - coins[i] >= 0:
                dp[i][a] += dfs(i, a - coins[i]) 
            
            return dp[i][a]

        return dfs(0, amount)



