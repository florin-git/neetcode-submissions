class Solution:
    # time: O(log x)
    # space: O(1)
    def reverse(self, x: int) -> int:
        num = abs(x)
        reverse = 0

        while num:
            reverse = (reverse * 10) + (num % 10)
            num = num // 10

            if reverse > 2 ** 31 - 1: # overflow
                return 0

        return reverse if x > 0 else -reverse