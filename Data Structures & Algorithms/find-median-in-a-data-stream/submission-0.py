class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        if not self.min_heap:
            self.min_heap.append(num)
            return

        if num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        
        if len(self.min_heap) > len(self.max_heap) + 1:
            elem = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -elem)
        elif len(self.min_heap) + 1 < len(self.max_heap):
            elem = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, elem)

    def findMedian(self) -> float:

        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2

        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        
        return -self.max_heap[0]
        

        
        