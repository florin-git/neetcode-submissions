class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def dfs(i, subset, target):

            if target == 0:
                res.append(subset.copy())
                return

            if target < 0:
                return 
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                subset.append(candidates[j])
                dfs(j + 1, subset, target - candidates[j])
                subset.pop()

        dfs(0, [], target)
        return res
                        
