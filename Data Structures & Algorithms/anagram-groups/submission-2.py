class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}
        for s in strs:
            freq_tuple = self.get_freq_tuple(s)
            if freq_tuple in anagrams:
                anagrams[freq_tuple].append(s)
            else:
                anagrams[freq_tuple] = [s]

        return list(anagrams.values())


    def get_freq_tuple(self, s: str) -> tuple[int]:
        arr = [0] * 26
        for c in s:
            i = ord(c) - ord ('a')
            arr[i] += 1

        return tuple(arr)