class Solution:
    # time: O(n * 4**n)
    # space: O(n * 4**n)
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        digit_letter_map = {
            "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        res = [""]
        for digit in digits:
            tmp = []
            for cur_str in res:
                for c in digit_letter_map[digit]:
                    tmp.append(cur_str + c)
            res = tmp   

        return res

            