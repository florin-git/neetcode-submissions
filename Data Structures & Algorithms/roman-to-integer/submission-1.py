class Solution:
    # time: O(n)
    # space: O(1)
    def romanToInt(self, s: str) -> int:

        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        integer = 0

        for i in range(len(s)):
            # if i < len(s) - 1 and (
            #     s[i] == "I" and s[i + 1] in {"V", "X"} or
            #     s[i] == "X" and s[i + 1] in {"L", "C"} or
            #     s[i] == "C" and s[i + 1] in {"D", "M"}
            # ):
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                integer -= roman_map[s[i]]
                continue
            
            integer += roman_map[s[i]]
        
        return integer
