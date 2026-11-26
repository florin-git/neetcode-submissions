class Solution:
    # time: O(n * 2^n + m), m = sum of the lengths of strings in worDict
    # space: O(m + 2^n)
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        cache = {}

        wordDict = set(wordDict)
        def dfs(i):

            if i >= len(s):
                return [""]

            if i in cache:
                return cache[i]

            res = []

            for j in range(i, len(s)):
                w = s[i: j + 1]
                if w not in wordDict:
                    continue

                strings = dfs(j + 1)
                if not strings:
                    continue

                for substr in strings:
                    sentence = w
                    if substr:
                        sentence += " " + substr

                    res.append(sentence)

            cache[i] = res
            return res
                

        return dfs(0)




