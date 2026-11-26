class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.dp(nums[:-1]), self.dp(nums[1:]))
    
    def dp(self, nums):
        if len(nums) == 1:
            return nums[0]

        first = nums[0]
        second = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = max(nums[i] + first, second)
            first = second
            second = temp

        return second
