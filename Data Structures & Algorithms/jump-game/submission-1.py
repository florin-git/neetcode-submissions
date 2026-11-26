class Solution:
    def canJump(self, nums: List[int]) -> bool:        
        # 1 2 0 1 0

        # 1 3 1 2 0 1


        def dfs(i):
            if i >= len(nums) - 1:
                return True

            max_num = min(nums[i], len(nums) - i)
            if max_num == len(nums) - 1:
                return True

            res = False
            for j in range(max_num, 0, -1):
                res = res or dfs(i + j)

            return res

        return dfs(0)


