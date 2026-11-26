class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq_map = self.build_frequency_map(s)
        
        for c in t:
            if c not in s_freq_map:
                return False

            # there are more chars in t than s
            if s_freq_map[c] == 0:
                return False

            s_freq_map[c] -= 1

        return True

    
    def build_frequency_map(self, s: str) -> dict:
        freq_map = {}

        for c in s:
            if c in freq_map:
                freq_map[c] += 1
            else:
                freq_map[c] = 1

        return freq_map