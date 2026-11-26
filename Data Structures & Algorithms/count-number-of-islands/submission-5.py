class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        num_islands = 0

        def dfs(r, c):

            if (
                r < 0 or c < 0 or
                r > ROWS - 1 or
                c > COLS - 1 or
                (r, c) in visited or
                grid[r][c] == "0"
            ):
                return

            visited.add((r, c))
            nei = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

            for a, b in nei:
                dfs(a, b)


        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    num_islands += 1

        return num_islands
