class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums.sort()

        def dfs(i, t, curr_list):

            if t < 0:
                return

            if t == 0:
                res.append(curr_list.copy())
                return

            for j in range(i, len(nums)):
                curr_list.append(nums[j])
                dfs(j, t - nums[j], curr_list)
                curr_list.pop()

        dfs(0, target, [])
        return res

            