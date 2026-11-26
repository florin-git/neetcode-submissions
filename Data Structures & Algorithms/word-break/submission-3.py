class Solution:
    ## Recursion
    # # time: O(t * m^n), n=len(s), m=len(wordDict), t=max(wordDict)
    # # space: O(n)
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:

    #     def dfs(i):
    #         if i == len(s):
    #             return True

    #         for w in wordDict:
    #             if (
    #                 (i + len(w)) <= len(s) and
    #                 s[i : i + len(w)] == w
    #             ):
    #                 if dfs(i + len(w)):
    #                     return True
    #         return False

    #     return dfs(0)

    # ## DP
    # # time: O(n * m * t)
    # # space: O(n)
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:

    #     memo = {len(s): True}

    #     def dfs(i):
    #         if i in memo:
    #             return memo[i]

    #         for w in wordDict:
    #             if (
    #                 (i + len(w)) <= len(s) and
    #                 s[i: i + len(w)] == w
    #             ):
    #                 if dfs(i + len(w)):
    #                     memo[i] = True
    #                     return True

    #         memo[i] = False
    #         return False

    #     return dfs(0)

    # # DP
    # # time: O((t^2 * n) + m)
    # # space: O(n + (m*t))
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     wordSet = set(wordDict)
    #     t = 0
    #     for w in wordDict:
    #         t = max(t, len(w))

    #     memo = {}
    #     def dfs(i):
    #         if i in memo:
    #             return memo[i]
    #         if i == len(s):
    #             return True
    #         for j in range(i, min(len(s), i + t)):
    #             if s[i : j + 1] in wordSet:
    #                 if dfs(j + 1):
    #                     memo[i] = True
    #                     return True
    #         memo[i] = False
    #         return False

    #     return dfs(0)

    # Memoization
    # time: 
    # space:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [False for i in range(len(s) + 1)]
        memo[-1] = True

        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    memo[i] = memo[i + len(w)]

                if memo[i]:
                    break

        return memo[0]










