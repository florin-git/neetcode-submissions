class Solution:
    # time: O(n * 2^n)
    # space: O(n)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()

        def dfs(i, curr_list, t):

            if t == 0:
                res.append(curr_list.copy())
                return

            if i >= len(candidates) or t < 0:
                return

            # include candidates[i]
            curr_list.append(candidates[i])
            dfs(i + 1, curr_list, t - candidates[i])
            curr_list.pop()
            
            # skip candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr_list, t)

        dfs(0, [], target)
        return res
        