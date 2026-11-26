class Solution:
    # # time: O(t * d^s), d=len(WordDict), t=max length of any word in worDict
    # # space: O(s)
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:

    #     def dfs(i):

    #         if i == len(s):
    #             return True

    #         for w in wordDict:
    #             if s[i: i + len(w)] == w:
    #                 if dfs(i + len(w)):
    #                     return True

    #         return False
        
    #     return dfs(0)


    # time: O(t * d^s), d=len(WordDict), t=max length of any word in worDict
    # space: O(s)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # cache[i] = if s[i:] can be segmented

        cache = {}
        cache[len(s)] = True

        def dfs(i):

            if i == len(s):
                return True
            
            if i in cache:
                return cache[i]

            for w in wordDict:
                if s[i: i + len(w)] == w:
                    if dfs(i + len(w)):
                        cache[i] = True
                        return True
            
            cache[i] = False
            return False
        
        return dfs(0) 
