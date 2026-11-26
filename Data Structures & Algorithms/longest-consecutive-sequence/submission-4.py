class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        unique_elements = set(nums)
        res = 0

        for n in nums:
            if n - 1 in unique_elements:
                continue

            i = n
            cur = 1
            while i + 1 in unique_elements:
                cur += 1 
                i = i + 1

            res = max(res, cur)

        return res
                