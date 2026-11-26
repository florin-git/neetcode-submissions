class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # find cases where the one at the left is smaller than the second
        # if it's not true increase the left
        # else increase the right

        l, r = 0, 1
        res = 0

        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            else:
                res = max(res, prices[r] - prices[l])

            r += 1

        return res