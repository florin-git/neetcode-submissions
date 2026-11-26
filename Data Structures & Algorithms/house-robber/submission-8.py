class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # cache = {}
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0

        #     if i in cache:
        #         return cache[i]

        #     pick = nums[i] + dfs(i + 2)
        #     not_pick = dfs(i + 1)

        #     cache[i] = max(pick, not_pick)
        #     return cache[i]

        # return dfs(0)
        if len(nums) == 1:
            return nums[0]

        # cache = [0 for _ in range(len(nums))]
        # cache[0] = nums[0]
        # cache[1] = max(nums[0], nums[1])

        # for i in range(2, len(nums)):
        #     pick = nums[i] + cache[i - 2]
        #     not_pick = cache[i - 1]
        #     cache[i] = max(pick, not_pick)

        # return cache[-1]

        first = nums[0]
        second = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = max(nums[i] + first, second)
            first = second
            second = temp

        return second







