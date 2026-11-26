class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        
        freq_map = Counter(hand)
        hand.sort()

        for n in hand:
            if freq_map[n]:
                for i in range(n, n + groupSize):
                    if i not in freq_map:
                        return False
                    freq_map[i] -= 1

        return True