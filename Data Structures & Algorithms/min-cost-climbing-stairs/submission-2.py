class Solution:
    # time: O(n)
    # space: O(1)
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        first = 0
        second = cost[-1]

        for i in range(len(cost) - 2, -1, -1):
            temp = cost[i] + min(first, second)
            first = second
            second = temp

        return min(first, second)

    #  def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     first = cost[-2]
    #     second = cost[-1]
        
    #     for i in range(len(cost) - 3, -1, -1):
    #         tmp = first
    #         first = cost[i] + min(first, second)
    #         second = tmp
            
    #     return min(first, second)