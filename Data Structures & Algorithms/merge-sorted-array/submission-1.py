class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # 0 0 10 20 20 40
        # 1 2

        
        for i in range(len(nums1) - 1, n - 1, -1):
            nums1[i] = nums1[i - n]

        i, j, k = 0, n, 0

        while j < len(nums1) and k < n:
            if nums1[j] < nums2[k]:
                nums1[i] = nums1[j]
                j +=1
            else:
                nums1[i] = nums2[k]
                k += 1
            i += 1

        while k < n:
            nums1[i] = nums2[k]
            k += 1
            i += 1

    
        