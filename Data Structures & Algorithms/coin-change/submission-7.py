class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = {}
        def dfs(t):
            if t == 0:
                return 0

            if t in cache:
                return cache[t]
            
            min_coins = float("inf")
            for c in coins:
                if t - c >= 0:
                    min_coins = min(min_coins, 1 + dfs(t - c))

            cache[t] = min_coins
            return min_coins

        res = dfs(amount)
        return -1 if res == float("inf") else res