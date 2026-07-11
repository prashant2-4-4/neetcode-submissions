from collections import Counter , defaultdict 
from typing import List

# this can be done in O(n) with Manacher's, which avoids redundant expansion by reusing palindrome radius info from already-computed centers
# slicing is O(n) time complexity so remeber it.
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        visited = []
        n = len(s)
        res = 0
        def expand(left , right):
            nonlocal res
            while left >= 0 and right < n and s[left]==s[right]:
                # if s[left:right+1] not in visited:
                    # print(s[left:right+1])
                # visited.append(s[left:right+1])
                res += 1
        
                left -= 1
                right += 1



        for i in range(n):
            expand(i , i) # expand around for odd
            expand(i , i+1) # expand around for even
        
        return res
        