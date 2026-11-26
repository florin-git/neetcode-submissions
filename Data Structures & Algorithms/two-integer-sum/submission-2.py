class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # time: O(n^2)
        # space: O(1)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        to_the_target = {}

        for i, n in enumerate(nums):
            diff = target - n 
            if n in to_the_target:
                return [to_the_target[n], i]

            to_the_target[diff] = i

        # [3,4,5,6] 7
