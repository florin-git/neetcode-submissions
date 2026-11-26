class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(curr_list, curr_nums):

            if len(curr_list) == len(nums):
                res.append(curr_list.copy())
                return

            for j in range(len(nums)):
                if nums[j] in curr_nums:
                    continue
                
                curr_nums.add(nums[j])
                curr_list.append(nums[j])
                
                dfs(curr_list, curr_nums)

                curr_nums.remove(nums[j])
                curr_list.pop()
        

        dfs([], set())
        return res

