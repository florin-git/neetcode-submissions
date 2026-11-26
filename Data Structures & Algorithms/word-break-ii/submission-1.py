class Solution:
    # # time: O(n^w)
    # # space: O(n^w)
    # def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
    #     res = []
    #     def dfs(i, curr_list):

    #         if i >= len(s):
    #             curr_str = " ".join(curr_list)
    #             res.append(curr_str)
    #             return

    #         for w in wordDict:
    #             if i + len(w) <= len(s) and s[i: i + len(w)] == w:
    #                 curr_list.append(w)
    #                 dfs(i + len(w), curr_list)
    #                 curr_list.pop()


    #     dfs(0, [])
    #     return res

    # time: O(n * 2^n + m), m = sum of the lengths of strings in worDict
    # space: O(m + 2^n)
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        res = []
        wordDict = set(wordDict)
        def dfs(i, curr_list):

            if i >= len(s):
                curr_str = " ".join(curr_list)
                res.append(curr_str)
                return

            for j in range(i, len(s)):
                if s[i: j + 1] in wordDict:
                    curr_list.append(s[i: j + 1])
                    dfs(j + 1, curr_list)
                    curr_list.pop()

        dfs(0, [])
        return res

                