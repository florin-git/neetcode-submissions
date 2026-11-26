class Solution:
    # time: O(n)
    # space: O(n)
    # Variant of Bucket Sort based on frequency
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        element_to_frequency_map = self.compute_frequency(nums)
        bucket = [[] for i in range(len(nums) + 1)]

        for n, freq in element_to_frequency_map.items():
            bucket[freq].append(n)

        top_k = []

        for i in range(len(bucket) - 1, 0, -1):
            top_k.extend(bucket[i])

            if len(top_k) == k:
                return top_k
         

    def compute_frequency(self, nums):
        freq = {}

        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        return freq
