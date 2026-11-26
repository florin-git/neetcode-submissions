class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        # anagrams = {}

        # # n * wlogw
        # for w in strs:
        #     sorted_w = "".join(sorted(w))
        #     if sorted_w in anagrams:
        #         anagrams[sorted_w].append(w)
        #     else:
        #         anagrams[sorted_w] = [w]

        # return list(anagrams.values())

        anagrams = {}

        for w in strs:
            chars = [0] * 26
            freq_map = Counter(w)
            for k,v in freq_map.items():
                chars[ord(k) - ord("a")] += v
            key = tuple(chars)

            if key in anagrams:
                anagrams[key].append(w)
            else:
                anagrams[key] = [w]

        return list(anagrams.values())
            


