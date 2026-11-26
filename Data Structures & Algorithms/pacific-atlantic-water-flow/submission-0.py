class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        pacific = set()
        atlantic = set()

    
        def dfs(r, c, visited, prev_height):

            if (
                r < 0 or c < 0 or
                r >= len(heights) or 
                c >= len(heights[0]) or
                (r, c) in visited or
                heights[r][c] < prev_height
            ):
                return
            
            visited.add((r, c))
            nei = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

            for a, b in nei:
                dfs(a, b, visited, heights[r][c])


        # add first and last rows
        for c in range(len(heights[0])):
            dfs(0, c, pacific, -1)
            dfs(len(heights) - 1, c, atlantic, -1)
        
        for r in range(len(heights)):
            dfs(r, 0, pacific, -1)
            dfs(r, len(heights[0]) - 1, atlantic, -1)
        

        return list(pacific & atlantic)
                    

















