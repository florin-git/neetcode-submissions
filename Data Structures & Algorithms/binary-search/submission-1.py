class Solution:

    # Recursive
    # time: O(log n)
    # space: O(1)
    def search(self, nums: List[int], target: int) -> int:

        def recursive(l, r):
            if l > r:
                return -1

            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m

            if nums[m] < target:
                return recursive(m + 1, r)
            
            return recursive(l, m - 1)

        return recursive(0, len(nums) - 1)





    # # Iterative
    # # time: O(log n)
    # # space: O(1)
    # def search(self, nums: List[int], target: int) -> int:

    #     l, r = 0, len(nums) -1

    #     while l <= r:
    #         m = (l + r) // 2
    #         if nums[m] == target:
    #             return m

    #         if nums[m] > target:
    #             r = m - 1
    #         else:
    #             l = m + 1

    #     return -1
        