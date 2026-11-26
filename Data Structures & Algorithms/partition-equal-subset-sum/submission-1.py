class Solution:
    # time: O(2**n)
    # space: O(n)
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if len(nums) <= 1 or tot % 2 == 1:
            return False

        target = tot // 2
        cache = {}
        def dfs(i, cur):
            nonlocal target
            if cur == target:
                return True

            if (i, cur) in cache:
                return cache[(i, cur)]

            if i >= len(nums):
                return False

            cache[(i, cur)] = dfs(i + 1, cur + nums[i]) or dfs(i + 1, cur)
            return cache[(i, cur)]

        return dfs(0, 0)
