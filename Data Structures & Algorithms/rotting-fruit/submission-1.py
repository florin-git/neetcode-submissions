class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        timer = 0
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()

                nei = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
                for i, j in nei:
                    if (
                        i < 0 or j < 0 or
                        i == ROWS or
                        j == COLS or
                        grid[i][j] == 0 or
                        grid[i][j] == 2
                    ):
                        continue

                    grid[i][j] = 2
                    q.append((i, j))
                    fresh -= 1

            timer += 1


        return timer if fresh == 0 else -1









