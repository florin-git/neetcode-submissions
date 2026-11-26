class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = set()
        candidates.sort()

        def dfs(i, curr_list, t):

            if t == 0:
                res.add(tuple(curr_list))
                return

            if i >= len(candidates) or t < 0:
                return

            curr_list.append(candidates[i])
            dfs(i + 1, curr_list, t - candidates[i])
            curr_list.pop()
            
            dfs(i + 1, curr_list, t)

        dfs(0, [], target)
        return [list(combination) for combination in res]
        