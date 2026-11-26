class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            
            num = (digits[i] + carry) // 10
            digits[i] = (digits[i] + carry) % 10
            carry = num

        if carry == 1:
            digits.insert(0, 1)

        return digits