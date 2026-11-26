class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        grid[-1][-1] = 1

        def dfs(i, j):
            if (
                i >= m or 
                j >= n
            ):
                return 0

            if (i, j) == (m - 1, n - 1):
                print("re")
                return 1

            nei = [(i + 1, j), (i, j + 1)]
            res = 0
            for r, c in nei:
                res += dfs(r, c)

            return res

        return dfs(0, 0)








