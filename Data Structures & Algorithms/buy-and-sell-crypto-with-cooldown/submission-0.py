class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # if len(prices) == 1:
            # return 0

        actions = {
            "buy": 1,
            "sell": 2,
            "skip": 3
        }


        def dfs(i, amount, prev_action):

            if i == len(prices):
                return amount # check

            if actions[prev_action] == 1: # buy
                sell = dfs(i + 1, amount + prices[i], "sell")
                skip = dfs(i + 1, amount, "buy")
                return max(sell, skip)
            elif actions[prev_action] == 2: # sell
                return dfs(i + 1, amount, "skip")
            elif actions[prev_action] == 3: # skip
                buy = dfs(i + 1, amount - prices[i], "buy")
                skip = dfs(i + 1, amount, "skip")
                return max(buy, skip)


        return dfs(0, 0, "skip")








        