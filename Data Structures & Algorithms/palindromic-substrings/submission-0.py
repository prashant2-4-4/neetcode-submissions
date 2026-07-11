from collections import Counter , defaultdict 
from typing import List
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        visited = []
        n = len(s)

        def expand(left , right):

            while left >= 0 and right < n and s[left]==s[right]:
                # if s[left:right+1] not in visited:
                    # print(s[left:right+1])
                visited.append(s[left:right+1])
        
                left -= 1
                right += 1



        for i in range(n):
            expand(i , i) # expand around for odd
            expand(i , i+1) # expand around for even
        
        return len(visited)
        