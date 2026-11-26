class Solution:
    # # time: O(n)
    # # space: O(n)
    # def trap(self, height: List[int]) -> int:
    #     if len(height) < 3:
    #         return 0

    #     max_left = [0 for _ in range(len(height))]
    #     max_right = [0 for _ in range(len(height))]
        
    #     for i in range(1, len(height)):
    #         max_left[i] = max(max_left[i - 1], height[i - 1])
    #     for i in range(len(height) - 2, -1, -1):
    #         max_right[i] = max(max_right[i + 1], height[i + 1])
        
    #     max_area = 0
    #     for i, h in enumerate(height):
    #         left = max_left[i]
    #         right = max_right[i]
    #         area = max(0, min(left, right) - h)
    #         max_area += area

    #     return max_area

    # time: O(n)
    # space: O(1)
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]

        res = 0
        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(max_left, height[l])
                res += max_left - height[l]
            else:
                r -= 1
                max_right = max(max_right, height[r])
                res += max_right - height[r]

        return res








        

