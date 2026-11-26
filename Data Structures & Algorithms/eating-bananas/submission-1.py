class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        max_num = max(piles)

        if h == len(piles):
            return max_num

        l, r = 1, max_num
        res = max_num

        while l <= r:
            k = l + (r - l) // 2
            time = self.compute_time(piles, k)

            if time > h:
                l = k + 1
            else:
                r = k - 1
                res = k

        return res


    def compute_time(self, piles, k):
        time = 0
        for b in piles:
            time += math.ceil(b / k)
        return time