class Solution:
    # time: O(n)
    # space: O(n)
    def maxProfit(self, prices: List[int]) -> int:

        dp = [[0 for _ in range(2)] for _ in range(len(prices) + 1)]

        for i in range(len(prices) - 1, -1, -1):
            for buying in [True, False]:
                cooldown = dp[i + 1][buying]
                if buying:
                    buy = dp[i + 1][False] - prices[i]
                    dp[i][buying] = max(buy, cooldown)
                else:
                    sell = prices[i]
                    if i + 2 < len(prices):
                        sell += dp[i + 2][True]  
                    dp[i][buying] = max(sell, cooldown)

        return dp[0][1]
