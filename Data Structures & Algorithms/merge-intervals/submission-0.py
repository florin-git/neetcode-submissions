class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        # sort by initial value

        # if end of the first is greater than beginning of second
        # -> [first beginnig, max(endings)]
        
        # move the second pointer while the above condition is true
        # then, add to the output the obtained interval


        intervals.sort()
        merged = []

        l, r = 0, 1

        while r < len(intervals): #check

            b1, e1 = intervals[l]
            b2, e2 = intervals[r]

            while e1 >= b2:
                b1, e1 = [b1, max(e1, e2)]

                r += 1
                if r >= len(intervals):
                    break
                
                b2, e2 = intervals[r]

            merged.append([b1, e1])
            l = r
            r += 1

        if r <= len(intervals):
            merged.append(intervals[l])

        return merged



