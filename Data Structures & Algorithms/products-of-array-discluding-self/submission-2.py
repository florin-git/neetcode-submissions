class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # 1 2 4 6
        # pre: 1 1 2 8
        # suf: 48 24 6 1


        pre = [1 for _ in range(len(nums))]
        suf = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]


        res = []
        for i in range(len(nums)):
            n = pre[i] * suf[i]
            res.append(n)
        return res