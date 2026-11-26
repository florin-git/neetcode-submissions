class Solution:
    # time: O(n*t)
    # space: O(t), where t is the amount
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[a] = minimum coins needed to make amount a
        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0

        for a in range(amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != float("inf") else -1 
