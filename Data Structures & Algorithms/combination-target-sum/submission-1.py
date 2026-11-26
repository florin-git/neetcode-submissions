class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(i, subset, t):
            
            if i == len(nums):
                if t == 0:
                    res.append(subset.copy())
                return

            if t < 0:
                return

            subset.append(nums[i])
            dfs(i, subset, t - nums[i])

            subset.pop()
            dfs(i + 1, subset, t)


        dfs(0, [], target)
        return res