class Solution:
    # time: O(n)
    # space: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # there is a gap where the number has no preceeding elements

        nums_set = {n for n in nums}

        res = 1
        for n in nums:
            if n - 1 in nums_set:
                continue

            num = n
            curr_res = 1
            while num + 1 in nums_set:
                curr_res += 1
                num = num + 1
            res = max(res, curr_res)

        return res