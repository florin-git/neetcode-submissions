class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Build a Counter for s
        s_counter = self.build_counter(s)

        for c in t:
            if c not in s_counter:
                return False

            if s_counter[c] == 0:
                return False 

            s_counter[c] -= 1

        return True


    def build_counter(self, s):

        counter = {}
        for c in s:
            if c not in counter:
                counter[c] = 1
            else:
                counter[c] += 1

        return counter
        