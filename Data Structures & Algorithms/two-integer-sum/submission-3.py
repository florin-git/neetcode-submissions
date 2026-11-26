class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # a + b = t
        # b = t - a

        second_num = {}
        for i, n in enumerate(nums):
            second_num[n] = i
        
        for j, n in enumerate(nums):
            diff = target - n
            if diff in second_num and second_num[diff] != j:
                return [j, second_num[diff]]
                
         