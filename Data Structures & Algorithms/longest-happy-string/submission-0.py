class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        

        letters = [[a, "a"], [b, "b"], [c, "c"]]
        consecutive = {
            "a": 0, "b": 0, "c": 0
        }

        s = []
        while True:
            letters.sort(key=lambda x: x[0], reverse=True)
            first = letters[0]
            second = letters[1]
            third = letters[2]

            if first[0] and consecutive[first[1]] < 2:
                s.append(first[1])
                first[0] -= 1
                consecutive[first[1]] += 1
                consecutive[second[1]] = 0
                consecutive[third[1]] = 0

            elif second[0] and consecutive[second[1]] < 2:
                s.append(second[1])
                second[0] -= 1
                consecutive[second[1]] += 1
                consecutive[first[1]] = 0
                consecutive[third[1]] = 0

            elif third[0] and consecutive[thirdthird[1]] < 2:
                s.append(third[1])
                third[0] -= 1
                consecutive[third[1]] += 1
                consecutive[first[1]] = 0
                consecutive[second[1]] = 0
            else:
                break

        return "".join(s)    



