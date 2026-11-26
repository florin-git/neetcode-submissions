class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def dfs(r, c):
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == 0
            ):
                return 1

            if (r, c) in visited:
                return 0

            visited.add((r, c))
            nei = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

            perimeter = 0
            for a, b in nei:
                perimeter += dfs(a, b)

            return perimeter


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c)

