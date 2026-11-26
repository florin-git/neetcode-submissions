class Solution:
    # # time: O(2^(m * n))
    # # space: O(m * n)
    # def uniquePaths(self, m: int, n: int) -> int:
    #     def dfs(i, j):
    #         if (
    #             i >= m or 
    #             j >= n
    #         ):
    #             return 0

    #         if (i, j) == (m - 1, n - 1):
    #             return 1

    #         nei = [(i + 1, j), (i, j + 1)]
    #         res = 0
    #         for r, c in nei:
    #             res += dfs(r, c)

    #         return res

    #     return dfs(0, 0)


    # time: O(m * n)
    # space: O(m * n)
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]


        def dfs(i, j):
            if (
                i >= m or 
                j >= n
            ):
                return 0

            if (i, j) == (m - 1, n - 1):
                return 1

            if memo[i][j] != -1:
                return memo[i][j]

            memo[i][j] =  dfs(i, j + 1) + dfs(i + 1, j)
            return memo[i][j]

        return dfs(0, 0)








