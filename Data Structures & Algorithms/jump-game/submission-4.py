class Solution:
    # time: O(n)
    # space: O(n)
    def canJump(self, nums: List[int]) -> bool:   

        cache = [False] * len(nums)
        cache[-1] = True
        
        for i in range(len(nums) - 2, -1, -1):
            max_num = min(nums[i], len(nums) - i)

            if max_num == len(nums) - i:
                cache[i] = True
                continue

            for j in range(max_num, 0, -1):
                cache[i] = cache[i] or cache[i + j]

        return cache[0]
