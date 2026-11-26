class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        l = 0
        res = float("-inf")

        cur = 0
        for r in range(len(nums)):
            cur += nums[r]

            res = max(res, cur)
            if cur < 0:
                # l = r + 1
                cur = 0

        return res