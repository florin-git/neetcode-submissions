class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        if len(nums) == 1:
            return nums[0]
        
        # build prefix sum with a function
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]

        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

    
        curr_sum = sum(nums[:k-1])
        res = float("-inf")

        for r in range(k - 1, len(nums)):
            curr_sum += nums[r]

            avg = curr_sum / (r + 1)
            res = max(res, avg)
            
            for l in range(r - k + 1):
                curr_sum -= prefix_sum[l]
                avg = curr_sum / (r - l)
                res = max(res, avg)

                # restore curr_sum
                curr_sum += prefix_sum[l]

        return res









