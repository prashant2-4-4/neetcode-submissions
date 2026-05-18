from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        n_s1 = len(s1)
        n_s2 = len(s2)

        while(left + n_s1 <= n_s2):
            if Counter(s1) == Counter(s2[left : left + n_s1]):
                return True
            left += 1
        
        return False