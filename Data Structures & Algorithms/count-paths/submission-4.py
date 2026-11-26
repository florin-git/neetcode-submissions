class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # cache = {}
        # def dfs(r, c):
        #     # out of bound return 0
        #     if (
        #         r < 0 or c < 0 or
        #         r >= m or c >= n
        #     ):
        #         return 0

        #     if r == m - 1 and c == n - 1:
        #         return 1

        #     if (r, c) in cache:
        #         return cache[(r, c)]

        #     cache[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
        #     return cache[(r, c)]

        # return dfs(0, 0)

        cache = [[0 for i in range(n + 1)] for _ in range(m + 1)]
        cache[m - 1][n - 1] = 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, - 1, -1):
                if r == m - 1 and c == n - 1:
                    continue
                cache[r][c] = cache[r + 1][c] + cache[r][c + 1]

        return cache[0][0]

