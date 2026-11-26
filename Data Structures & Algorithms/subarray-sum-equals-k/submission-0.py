class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sum_count_map = defaultdict(int)
        sum_count_map[0] = 1

        res = 0
        curr_sum = 0
        for n in nums:
            curr_sum += n

            diff = curr_sum - k
            if diff in sum_count_map:
                res += sum_count_map[diff]

            sum_count_map[curr_sum] += 1

        return res

