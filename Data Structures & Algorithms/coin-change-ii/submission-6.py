class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        cache = {}
        def dfs(i, a):

            if a == 0:
                return 1

            if (i, a) in cache:
                return cache[(i, a)]

            res = 0
            for j in range(i, len(coins)):
                if a - coins[j] >= 0:
                    res += dfs(j, a - coins[j])
            
            cache[(i, a)] = res
            return res

        return dfs(0, amount)