
class UF:
    def __init__(self, n: int):
        self.parents = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.comps = n

    def find(self, node):
        cur = node
        while cur != self.parents[cur]:
            self.parents[cur] = self.parents[self.parents[cur]]
            cur = self.parents[cur]

        return cur

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        self.comps -= 1
        if self.size[pv] > self.size[pu]:
            pu, pv = pv, pu

        self.size[pu] += self.size[pv]
        self.parents[pv] = pu
        return True

    def components(self):
        return self.comps


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # too many edges -> cycle
        if len(edges) > n - 1:
            return False 

        uf = UF(n)
        for a, b in edges:
            if not uf.union(a, b):
                return False

        return uf.components() == 1

        


        