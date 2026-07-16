from collections import deque , Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        keys = sorted(hand)
        count = Counter(hand)
        for card in keys:
            while count[card] > 0:
                for nxt in range(card , card+groupSize):
                    if count[nxt] > 0:
                        count[nxt] -= 1
                    
                    else:
                        return False
        return True



