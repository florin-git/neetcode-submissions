class Solution:
    # # Union Find
    # # time: O(v + (e * alpha(v))), alpha is used for amortized complexity
    # # space: O(v)
    # def countComponents(self, n: int, edges: List[List[int]]) -> int:
    #     # Each node it's parent of itself
    #     par = [i for i in range(n)]
    #     rank = [1] * n

    #     # finds root parent of a node
    #     def find(n1):
    #         res = n1

    #         # stop when the parent is itself
    #         while res != par[res]:
    #             par[res] = par[par[res]] # path compression
    #             res = par[res]

    #         return res

    #     # union the components of n1 and n2
    #     def union(n1, n2):
    #         p1, p2 = find(n1), find(n2)

    #         if p1 == p2:
    #             return 0

    #         if rank[p2] > rank[p1]:
    #             par[p1] = p2
    #             rank[p2] += rank[p1]
    #         else:
    #             par[p2] = p1
    #             rank[p1] += rank[p2]
    #         return 1

    #     res = n
    #     for n1, n2 in edges:
    #         res -= union(n1, n2)

    #     return res



    # Union Find
    # time: O(v + (e * alpha(v))), alpha is used for amortized complexity
    # space: O(v)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        num_components = n
        for u, v in edges:
            if dsu.union(u, v):
                num_components -= 1
        return num_components




class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u]) # path compression
        return self.parent[u]


    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu # attach smaller tree to higher
        elif self.rank[pv] < self.rank[pv]:
            self.parent[pu] = pv
        else:
            self.parent[pu] = pv
            self.rank[pu] += 1

        return True

    







