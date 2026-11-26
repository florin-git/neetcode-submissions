class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        max_left = [0 for _ in range(len(height))]
        max_right = [0 for _ in range(len(height))]
        
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i - 1], height[i - 1])
        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])
        
        max_area = 0
        for i, h in enumerate(height):
            left = max_left[i]
            right = max_right[i]
            area = max(0, min(left, right) - h)
            max_area += area

        return max_area

        # extreme values (strictly) higher than inner values
        # base = number of inner values
        # height = min extreme values 

        # area = (base * height) - inner values

        # I'd like to know which is the max value at the left of value
        # at index i. Same at the right

        # the max on the extreme should be greater than me
        

