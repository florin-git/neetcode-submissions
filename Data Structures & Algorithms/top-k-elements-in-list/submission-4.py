class Solution:

    from collections import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = self.build_frequency_map(nums)
        freq_list = [[v, k] for k, v in freq_map.items()]


        heap = freq_list[:k]
        heapq.heapify(heap)

        for i in range(k, len(freq_list)):
            new_freq = freq_list[i][0]
            min_freq = heap[0][0]

            if new_freq > min_freq:
                heapq.heappop(heap)
                heapq.heappush(heap, freq_list[i])

        return [k for (v, k) in heap]



    def build_frequency_map(self, nums: List[int]) -> dict[int, int]:
        freq_map = {}
        for n in nums:
            if n in freq_map:
                freq_map[n] += 1
            else:
                freq_map[n] = 1

        return freq_map
        