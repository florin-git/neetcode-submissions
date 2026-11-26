class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:

    #     visited = set()
    #     num_islands = 0

    #     def dfs(i, j):

    #         if ((i, j) in visited or
    #             i < 0 or j < 0 or
    #             i >= len(grid) or j >= len(grid[0]) or
    #             grid[i][j] == "0"
    #         ):
    #             return

    #         visited.add((i, j))
    #         nei = [[i+1, j], [i-1, j], [i, j-1], [i, j+1]]

    #         for a, b in nei:
    #             dfs(a, b)



    #     for r in range(len(grid)):
    #         for c in range(len(grid[0])):
    #             if grid[r][c] == "1" and (r, c) not in visited:
    #                 num_islands += 1

    #                 dfs(r, c)

    #     return num_islands


    def numIslands(self, grid: List[List[str]]) -> int:

        from collections import deque

        visited = set()
        num_islands = 0

        def bfs(i, j):
            q = deque()
            visited.add((i, j))
            q.append((i, j))

            while q:
                # r, c = q.popleft()
                r, c = q.pop() 

                nei = [[r+1, c], [r-1, c], [r, c-1], [r, c+1]]

                for a, b in nei:
                    if (
                        (a, b) not in visited and
                        a in range(len(grid)) and
                        b in range(len(grid[0])) and
                        grid[a][b] == "1"
                    ):
                        q.append((a, b))
                        visited.add((a, b))
                

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    num_islands += 1

                    bfs(r, c)

        return num_islands
        