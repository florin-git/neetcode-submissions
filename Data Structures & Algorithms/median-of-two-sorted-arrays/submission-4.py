class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # the medium is the element having the same numeber of elements to its left and
        # to its right

        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            A_left = A[i] if i >= 0 else float("-inf")
            A_right = A[i + 1] if (i + 1) < len(A) else float("inf")

            B_left = B[j] if j >= 0 else float("-inf")
            B_right = B[j + 1] if (j + 1) < len(B) else float("inf")

            # check out of bound
            if A_left > B_right:
                r = i - 1
            elif B_left > A_right:
                l = i + 1
            else:
                break

        if total % 2 == 0:
            return (max(A_left, B_left) + min(A_right, B_right)) / 2
        
        return min(A_right, B_right)






















        