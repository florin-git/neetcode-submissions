class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0
        visited = set()

        def dfs(r, c):
            nonlocal res

            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visited or
                grid[r][c] == 0
            ):
                return 0

            visited.add((r, c))

            nei = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            area = 1
            for a, b in nei:
                area += dfs(a, b)

            res = max(res, area)    
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)

        return res








            