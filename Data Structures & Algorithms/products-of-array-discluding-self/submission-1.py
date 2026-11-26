class Solution:
    # # time: O(n)
    # # space: O(n)
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
        
    #     product_left = [1] * len(nums)
    #     product_right = [1] * len(nums)

    #     for i in range(1, len(nums)):
    #         product_left[i] = product_left[i - 1] * nums[i - 1]

    #     for i in range(len(nums) - 2, -1, -1):
    #         product_right[i] = product_right[i + 1] * nums[i + 1]

    #     for i in range(len(nums)):
    #         product_left[i] *= product_right[i]

    #     return product_left

    # time: O(n)
    # space: O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res




