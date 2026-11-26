class Solution:
    # # time: O(2^n)
    # # space: O(n), where n is the amount/(smallest coin)
    # def coinChange(self, coins: List[int], amount: int) -> int:

    #     def dfs(i, a, cur) -> int:
    #         if i >= len(coins) or a < 0:
    #             return float("inf")

    #         if a == 0:
    #             return cur

    #         pick = dfs(i, a - coins[i], cur + 1) # choose current

    #         not_pick = dfs(i + 1, a, cur) # skip current

    #         return min(pick, not_pick)

    #     res = dfs(0, amount, 0)
    #     return res if res != float("inf") else -1


    # # time: O(n)
    # # space: O(n), where n is the amount/(smallest coin)
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     # dp[(i, a)] = minimum coins needed to make amount a using coins from index i onwards
    #     dp = {}

    #     def dfs(i, a) -> int:
    #         # Base cases
    #         if a == 0:
    #             return 0  # No coins needed for amount 0
            
    #         if i >= len(coins) or a < 0:
    #             return float("inf")  # Invalid state
            
    #         # Check cache with BOTH i and a as the key
    #         if (i, a) in dp:
    #             return dp[(i, a)]
            
    #         # Option 1: Pick current coin (stay at index i, can pick again)
    #         pick = 1 + dfs(i, a - coins[i])
            
    #         # Option 2: Skip current coin (move to next coin)
    #         not_pick = dfs(i + 1, a)
            
    #         # Store the minimum in cache
    #         dp[(i, a)] = min(pick, not_pick)
    #         return dp[(i, a)]
        
    #     res = dfs(0, amount)
    #     return res if res != float("inf") else -1

    # time: O(n)
    # space: O(n), where n is the amount/(smallest coin)
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[a] = minimum coins needed to make amount a
        dp = {}

        def dfs(a) -> int:            
            if a == 0:
                return 0  # No coins needed for amount 0

            if a < 0:
                return float("inf")

            if a in dp:
                return dp[a]

            min_coins = float("inf")
            for c in coins:
                min_coins = min(min_coins, 1 + dfs(a - c))

            dp[a] = min_coins
            
            return dp[a]
        
        res = dfs(amount)
        return res if res != float("inf") else -1


