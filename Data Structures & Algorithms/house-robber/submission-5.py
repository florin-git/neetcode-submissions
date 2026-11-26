class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = {}
        def dfs(i):
            if i >= len(nums):
                return 0

            if i in cache:
                return cache[i]

            pick = nums[i] + dfs(i + 2)
            not_pick = dfs(i + 1)

            cache[i] = max(pick, not_pick)
            return cache[i]

        return dfs(0)