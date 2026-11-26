class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(cur, already_chosen):

            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            
            for i in range(len(nums)):
                if nums[i] in already_chosen:
                    continue
                    
                cur.append(nums[i])
                already_chosen.add(nums[i])

                dfs(cur, already_chosen)

                cur.pop()
                already_chosen.remove(nums[i])

        dfs([], set())
        return res


        
        
            
