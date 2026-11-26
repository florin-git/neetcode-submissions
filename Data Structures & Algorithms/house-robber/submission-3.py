class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = nums + [0]

        for i in range(len(nums) - 3, -1, -1):
            cache[i] = max(nums[i] + cache[i + 2], cache[i + 1])

        return max(cache[0], cache[1])