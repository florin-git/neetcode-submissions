class Solution:
    def isPalindrome(self, x: int) -> bool:
        

        # 1 2 3

        # 3 2 1

        # 3 * 10 + 2
        # 32 * 10 + 1
        # 11

        reversed_x = 0
        original_x = x
        while x > 0:
            remainder = x % 10
            reversed_x = reversed_x * 10 + remainder

            x = x // 10

        return reversed_x == original_x
