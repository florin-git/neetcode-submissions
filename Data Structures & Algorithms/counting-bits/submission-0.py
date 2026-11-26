class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            offset = 2 ** math.floor(math.log2(i))
            res[i] = 1 + res[i - offset]
        return res

