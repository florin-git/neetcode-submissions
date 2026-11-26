class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if len(nums) <= 1 or tot % 2 == 1:
            return False

        target = tot // 2

        def dfs(i, cur):
            nonlocal target
            if cur == target:
                return True

            if i >= len(nums):
                return False

            return dfs(i + 1, cur + nums[i]) or dfs(i + 1, cur)

        return dfs(0, 0)


        # nums.sort()
        # l, r = 0, len(nums) - 1

        # cur = 0
        # for i in range(len(nums) - 1, -1, -1):
        #     if cur + nums[i] == target:
        #         return True
        #     elif cur + nums[i] < target:
        #         cur += nums[i]

        # return False