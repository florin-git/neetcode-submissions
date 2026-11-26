class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        i = self.first_greater_or_equal(arr, x)
        l, r = i - 1, i
        res = []

        l, r = i - 1, i
        while r - l - 1 < k:
            if l < 0:
                r += 1
            elif r >= len(arr):
                l -= 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1
            else:
                r += 1

        return arr[l + 1:r]


    def first_greater_or_equal(self, arr: list[int], x: int) -> int:

        l, r = 0, len(arr) - 1
    
        while l < r:
            m = (l + r) // 2

            if arr[m] < x:
                l = m + 1
            else: # elif arr[m] > x:
                r = m

        return l