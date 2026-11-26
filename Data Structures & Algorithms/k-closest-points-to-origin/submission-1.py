class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        max_heap = []
        for p in points:
            # I negate for managing a max heap
            neg_square_diff = -self.compute_square_difference(p, [0, 0])
            heapq.heappush(max_heap, (neg_square_diff, p))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [p for _, p in max_heap]

        

        
    def compute_square_difference(self, p1: list[int], p2: list[int]) -> float:
        res = 0
        for i in range(len(p1)):
            res += (p1[i] - p2[i]) ** 2

        return res