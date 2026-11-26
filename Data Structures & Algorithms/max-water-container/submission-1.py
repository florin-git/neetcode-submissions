class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        res = 0

        # 1 7 2 5 4 7 3 6

        while l < r:
            base = r - l #+ 1
            area = base * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1


        return res