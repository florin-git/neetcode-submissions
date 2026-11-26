class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # I negate for managing a max heap
        neg_square_diff = [
            (-self.compute_square_difference(p, [0, 0]), p)
            for p in points
        ]
        # 0 5 2 1
        heapq.heapify(neg_square_diff)

        while len(neg_square_diff) > k:
            heapq.heappop(neg_square_diff)

        return [p for _, p in neg_square_diff]

        

        
    def compute_square_difference(self, p1: list[int], p2: list[int]) -> float:
        res = 0
        for i in range(len(p1)):
            res += (p1[i] - p2[i]) ** 2

        return res