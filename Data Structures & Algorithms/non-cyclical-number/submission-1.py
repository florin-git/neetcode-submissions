class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}

        while n != 1:

            new_n = 0
            while n:
                new_n += (n % 10) ** 2
                n = n // 10
            
            if new_n in seen:
                return False 
            seen.add(new_n)
            n = new_n
        return True