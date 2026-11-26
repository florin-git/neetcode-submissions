class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        area = 0
        visited = set()

        def dfs(r, c):

            if (
                r < 0 or c < 0 or
                r >= len(grid) or
                c >= len(grid[0]) or
                (r, c) in visited or
                grid[r][c] == 0
            ):
                return 0

            visited.add((r, c))
            nei = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

            res = 1
            for a, b in nei:
                res += dfs(a, b)

            return res

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res = dfs(r, c)
                    area = max(area, res)

        return area



