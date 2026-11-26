class Solution:
    # def maxProfit(self, prices: List[int]) -> int:

    #     actions = {
    #         "buy": 1,
    #         "sell": 2,
    #         "skip": 3
    #     }

    #     def dfs(i, amount, prev_action):

    #         if i == len(prices):
    #             return amount # check

    #         if actions[prev_action] == 1: # buy
    #             sell = dfs(i + 1, amount + prices[i], "sell")
    #             skip = dfs(i + 1, amount, "buy")
    #             return max(sell, skip)
    #         elif actions[prev_action] == 2: # sell
    #             return dfs(i + 1, amount, "skip")
    #         elif actions[prev_action] == 3: # skip
    #             buy = dfs(i + 1, amount - prices[i], "buy")
    #             skip = dfs(i + 1, amount, "skip")
    #             return max(buy, skip)


    #     return dfs(0, 0, "skip")

    # # time: O(2^n)
    # # space: O(n)
    # def maxProfit(self, prices: List[int]) -> int:

    #     def dfs(i, buying):
    #         if i >= len(prices):
    #             return 0

    #         cooldown = dfs(i + 1, buying)
    #         if buying:
    #             buy = dfs(i + 1, not buying) - prices[i]
    #             return max(buy, cooldown)
    #         else:
    #             sell = dfs(i + 2, not buying) + prices[i]
    #             return max(sell, cooldown)

    #     return dfs(0, True)


    # time: O(2^n)
    # space: O(n)
    def maxProfit(self, prices: List[int]) -> int:

        dp = [[-1 for _ in range(len(prices) + 1)] for _ in range(2)]

        def dfs(i, buying):
            if i >= len(prices):
                return 0

            if dp[buying][i] != -1:
                return dp[buying][i]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[buying][i] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[buying][i] = max(sell, cooldown)

            return dp[buying][i]

        return dfs(0, True)








        