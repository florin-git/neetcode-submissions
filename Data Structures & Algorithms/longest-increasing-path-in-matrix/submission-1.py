class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        cache = {}

        def dfs(r, c, prev):

            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                matrix[r][c] <= prev
            ):
                return 0

            if (r, c) in cache:
                return cache[(r, c)]


            nei = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

            res = 1
            for i, j in nei:
                res = max(res, 1 + dfs(i, j, matrix[r][c]))

            cache[(r, c)] = res
            return res

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, -1))

        return res







