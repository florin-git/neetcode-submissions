class Solution:
    # time: O(t * d^s), d=len(WordDict), t=max length of any word in worDict
    # space: O(s)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # cache[i] = if s[i:] can be segmented

        cache = [False for _ in range(len(s) + 1)]
        cache[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s)) and s[i: i + len(w)] == w:
                    cache[i] = cache[i + len(w)]
                    if cache[i]:
                        break


        return cache[0]
