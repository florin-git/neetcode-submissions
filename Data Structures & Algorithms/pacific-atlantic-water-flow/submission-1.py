class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, prev, visited):

            if (
                r < 0 or c < 0 or
                r >= ROWS or
                c >= COLS or
                (r, c) in visited or
                heights[r][c] < prev
            ):
                return

            visited.add((r, c))
            nei = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

            for i, j in nei:
                dfs(i, j, heights[r][c], visited)

        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, COLS - 1, heights[r][COLS - 1], atlantic)
        
        for c in range(COLS):
            dfs(0, c, heights[0][c], pacific)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], atlantic)
            # pacific.add((0, c))
            # atlantic.add((0, COLS - 1))

        return list(pacific & atlantic)









