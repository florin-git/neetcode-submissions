class Solution:
    # def canJump(self, nums: List[int]) -> bool:        
    #     def dfs(i):
    #         if i >= len(nums) - 1:
    #             return True

    #         max_num = min(nums[i], len(nums) - i)
    #         if max_num == len(nums) - 1:
    #             return True

    #         res = False
    #         for j in range(max_num, 0, -1):
    #             res = res or dfs(i + j)

    #         return res

    #     return dfs(0)


    def canJump(self, nums: List[int]) -> bool:   

        cache = {}
     
        def dfs(i):
            if i >= len(nums) - 1:
                return True

            if i in cache:
                return cache[i]

            max_num = min(nums[i], len(nums) - i)
            if max_num == len(nums) - 1:
                return True

            res = False
            for j in range(max_num, 0, -1):
                res = res or dfs(i + j)

            cache[i] = res
            return res

        return dfs(0)


