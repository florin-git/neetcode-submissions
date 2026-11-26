class Solution:
    # Recursive Binary Search
    def search(self, nums: List[int], target: int) -> int:
        return self.recursive_search(0, len(nums) - 1, nums, target)


    def recursive_search(self, l: int, r: int, nums: list[int], target: int) -> int:
        if l > r:
            return -1

        m = l + (r - l) // 2

        if nums[m] == target:
            return m

        if nums[m] < target:
            return self.recursive_search(m + 1, r, nums, target)
        
        return self.recursive_search(l, m - 1, nums, target)

        
