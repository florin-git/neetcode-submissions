class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        res = []
        def dfs(i, curr_list):

            if i >= len(s):
                curr_str = " ".join(curr_list)
                res.append(curr_str)
                return


            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i + len(w)] == w:
                    curr_list.append(w)
                    dfs(i + len(w), curr_list)
                    curr_list.pop()


        dfs(0, [])
        return res

                