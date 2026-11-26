class Solution:
    # # time: O(n * a)
    # # space: O(a)
    # def change(self, amount: int, coins: List[int]) -> int:
    #     prev = [0 for _ in range(amount + 1)]
    #     curr = [0 for _ in range(amount + 1)]

    #     prev[0], curr[0] = 1, 1
        
    #     for i in range(len(coins) -1, -1, -1):
    #         for a in range(amount + 1):
    #             curr[a] = prev[a]
    #             if a - coins[i] >= 0:
    #                 curr[a] += curr[a - coins[i]]

    #         prev = curr

    #     return prev[amount]


    # time: O(n * a)
    # space: O(a)
    def change(self, amount: int, coins: List[int]) -> int:
        curr = [0 for _ in range(amount + 1)]
        curr[0] = 1
        
        for i in range(len(coins) -1, -1, -1):
            for a in range(amount + 1):
                if a - coins[i] >= 0:
                    curr[a] += curr[a - coins[i]]

        return curr[amount]
        