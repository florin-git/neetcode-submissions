class Solution:
    def trap(self, height: List[int]) -> int:

        # if after greater or equal -> update amount and reset
        # update the final result only if I find something heigher later
        
        # 0 2 2 3 3 3 3 3 3 3
        # 2 2 3 3 3 3 3 3 2 1
        left_heigher = [height[0]] * len(height)
        right_heigher = [height[-1]] * len(height)
  

        for i in range(1, len(height)):
            left_heigher[i] = max(left_heigher[i - 1], height[i])

        for i in range(len(height) - 2, -1, -1):
            right_heigher[i] = max(right_heigher[i + 1], height[i])

        res = 0
        for i in range(len(height)):
            res += min(left_heigher[i], right_heigher[i]) - height[i]

        return res
