from typing import List
import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(l, r):
            if l >= r:
                return

            # Pick random pivot to prevent worst-case on sorted data
            pivot_idx = random.randint(l, r)
            pivot = nums[pivot_idx]

            # 3-way partition (Dutch National Flag algorithm)
            # Elements < pivot move left of `lt`
            # Elements == pivot sit between `lt` and `i - 1`
            # Elements > pivot move right of `gt`
            lt, i, gt = l, l, r
            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:
                    i += 1

            # Recurse only on strictly smaller and strictly larger sections
            quicksort(l, lt - 1)
            quicksort(gt + 1, r)

        quicksort(0, len(nums) - 1)
        return nums