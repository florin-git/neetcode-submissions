class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # n = len(strs)
        # m = avg(len(s)), for s in strs

        # O(n * mlogm)

        # O(n**2 * m)

        # iterate over the strings
        # sort the string
        # check in the dictionary
        #     if match append
        #     else create sublist

        anagrams = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in anagrams:
                anagrams[sorted_s].append(s)
            else:
                anagrams[sorted_s] = [s]

        return list(anagrams.values())




