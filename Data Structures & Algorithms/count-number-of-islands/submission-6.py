
# Disjoint Set Union
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * (n + 1)

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        if self.size[pu] > self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv

        return True


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dsu = DSU(ROWS * COLS)

        def index(r, c):
            return r * COLS + c

        
        num_islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "0":
                    continue

                num_islands += 1
                nei = [[r+1, c], [r-1, c], [r, c-1], [r, c+1]]
                for a, b in nei:
                    if (
                        a < 0 or b < 0 or
                        a >= ROWS or b >= COLS or
                        grid[a][b] == "0"
                    ):
                        continue

                    if dsu.union(index(r, c), index(a, b)):
                        num_islands -= 1

        return num_islands










