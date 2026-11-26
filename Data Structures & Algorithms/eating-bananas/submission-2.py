class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        m = max(piles)
        l, r = 1, m
        res = 0

        while l <= r:
            k = (l + r) // 2
            is_valid = self.check_with_k(piles, h, k)

            if is_valid:
                r = k - 1
                res = k
            else:
                l = k + 1

        return res


    
    def check_with_k(self, piles: list[int], h: int, k: int) -> bool:

        count = 0
        for p in piles:
            count += math.ceil(p / k)

        return count <= h
