class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                grid[r][c] = min(grid[r][c], dist)

                nei = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                for i, j in nei:
                    if (
                        i in range(ROWS) and
                        j in range(COLS) and
                        (i, j) not in visited and
                        grid[i][j] != -1
                    ):
                        q.append((i, j))
                        visited.add((i, j))

            dist += 1

    




